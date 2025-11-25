## Foresight
- 论文名称：Foresight-a generative pretrained transformer for modelling of patient timelines using electronic health records a retrospective modelling study
### 一、目的
- 基于电子健康记录的患者时间线时序建模，并预测未来相关医学事件（包括疾病、医疗操作、物质相关时间等，都是从医疗预料库中抽取）。
- 三个重点：  
①电子健康记录，包括结构化数据（例如年龄、性别等个人资料，血常规等量化实验数据）和非结构化数据（例如影响报告、医生诊疗报告等没有统一结构的，不好直接输入给计算机的数据）。目前对非结构化数据处理不怎么好，但重要信息都出自这里，所以此模型想要设计一个能将非结构化数据转为结构编码的方法。  
②时间线时序建模。模型需要聚焦时间线。  
③预测未来事件。目前模型最多预测未来几个月的事件，此模型想要设计一个预测事件更长远的方法。
### 二、主要架构
#### 1.数据检索与预处理
- 论文中主要使用3个数据集（KCH、SLaM、MIMIC-III），先从中提取EHR（患者电子健康记录）的数据。
#### 2.非结构数据转化为结构编码（MedCAT）
- 其中一个核心，用MedCAT将非结构化数据转化为结构编码，和结构数据共同组成输入的时间线序列。
#### 3.因果语言建模，自回归生成（GPT-2）
- GPT-2采用decoder架构，简单来说就是通过前面的序列生成后续token（从词库中抽取预测概率最大的，一开始随机抽取）。
- 对比bert等双向掩码：双向掩码由于可以看到未来信息，有作弊的可能性，最后泛化能力可能不强。
- 对比lstm（长短时神经网络）：在MIMIC数据集上GPT-2比它的准确率高出了40%左右（论文数据）。lstm对于时间线敏感，可解释性强，在时间线不是特别长且数据量小的情况下表现可能会比较好；GPT-2可解释性差（只是算下一个词的概率），但在数据量大的时候准确率可观。
#### 3.可视化web
- 链接：https://foresight.sites.er.kcl.ac.uk/
- 提供交互功能，手动添加时间线并查看预测结构。
### 三、论文总结
- 主要重点在于**非结构化数据处理**（MedCAT）以及**模型构建**（GPT-2）
- 自己粗略实验结果：用压缩版本的MIMIC数据集，775个样本，训练20轮后，GPT-2比LSTM准确率高41.2%；改成200后，GPT-2比LSTM低73.3%。
### 四、代码研究
#### 1.experiments/Foresight | MIMIC | Final | Prepare data.ipynb(预处理数据)
##### 输入：  
###### ①原始注释数据（MIMIC-III电子病历）  
- 路径：./data/timecat/mimic/annotated_february_2022/part_*.pickle  
- 内容：MedCat对MIMIC数据库中临床文本NOTEEVENTS.CSV的注释结果  
###### ②辅助映射文件  
- doc2pt.pickle:文档ID->患者ID映射  
- doc2time.pickle:文档ID->时间戳  
- pt2dob_datetime.pickle：患者ID->死亡时间戳
- pt2sex.pickle：患者ID->性别
- pt2ethnicity.pickle:患者ID->种族/民族
###### ③MedCAT模型包
- mc_modelpack_phase2_snomed_190k_february_2022.zip
##### 输出
- dataset-info/{RUN_NAME}.txt 数据集统计信息（患者数、概念数、各类别数量等）
- dataset-info/{RUN_NAME}.html 序列长度分布直方图
- {RUN_NAME}_just_before_encoding/ 编码前的 Hugging Face Dataset（含 token 字符串、时间、类型等）
- {RUN_NAME}_prepared_split/ 最终编码后的数据集
- tokenizer_{RUN_NAME}.pickle 自定义 tokenizer
- lns_{DATASET_NAME}.pickle 各患者 stream 长度列表
- cnts_{DATASET_NAME}.pickle 各 token 的全局出现频次
- types_{DATASET_NAME}.pickle 每种 token_type 对应的 token 集合
##### 所需资料
- mimic-iii数据集（已有）
- MedCAT模型包（只有公开的）
ps: SNOMED-CT知识库(已有),是自己构建MedCAT需要的，但自己构建太复杂了，一直失败。
### 五、当前问题
- 没有论文中使用的MedCAT模型包（是私有的），找到了公开模型包MedMentions（从公开数据集MedMentions构建），如果能拿到从SNOMED-CT构建的模型包更好（需通过NIH认证）
- 之前尝试自己构建模型包，但不能用，代码一直报错。（自己构建非常复杂，靠ai行不通，得学习官方文档）
- 用公开模型包MedMentions，发生了很多key不匹配的问题。