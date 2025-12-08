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
# ETHOS
## 一、目的
- 构建一个无需标注数据、无需任务微调的通用医疗基础模型，能够以零样本（zero-shot）方式预测患者个体化的未来健康轨迹（health trajectory）。
## 二、主要架构
### 1.患者健康时间线（PHT）的统一数据表示
- 将 MIMIC-IV 中12 类异构表（诊断、用药、检验、生命体征、ICU记录等）按精确时间戳（患者年龄，64位浮点）排序；
- 构成一条因果、时序、结构化的事件序列；
- 移除原始时间戳，仅保留事件顺序和相对时间间隔。
### 2.医学感知的Tokenization策略
PHT 中的每个事件被转化为 1–7 个具有医学语义的 token：
- 静态信息（前6位）：性别、种族、BMI、出生年代、PHT起始年代（5年粒度）；
- 数值变量 → 十分位 token（Q1–Q10）：所有连续值（如肌酐、血压）按训练集十分位离散化，模型自动学习其临床顺序；
- 标准编码分层 tokenization：
ATC 药物码（如 A10BA02）→ [A10][B][A02]
ICD-10 诊断/操作码 → 按字符层级拆分为多个 token；
- 时间间隔 token（13类）：如 5m, 1h, 1d, 6m，显式建模时间语义；
特殊事件 token：如 [入院], [死亡], [ICU], [SOFA], [DRG]。
### 3.模型：ETHOS Transformer
- 基于 GPT-2 解码器架构（纯自回归）；
- 上下文窗口：2048 个 token；
位置编码：可学习嵌入（非正弦函数）；
- 训练方式：无监督语言建模——仅预测下一 token；
- 训练资源：8×GPU，36 小时（MIMIC-IV v2.2，>20万患者，>40万次住院）。
### 4.零样本推理机制
- 输入：患者历史 PHT（截至某时间点，如入院）；
- 生成：多次（默认20次）自回归生成 fPHT（未来健康时间线）；
- 预测：通过统计 fPHT 中特定 token 的出现频率或位置，完成各类任务：
死亡率 → “死亡”token 出现比例；
- ICU 住院日 → 累加时间间隔 token 直至“ICU 出院”；
- SOFA 评分 → 读取 SOFA 后的 Q-token 概率，加权平均对应分位均值；
DRG 分类 → 读取出院后 DRG token 的 top-1 概率（771 类，准确率 84.8%）。