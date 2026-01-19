import os
import pandas as pd

# === 配置区 ===
MIMIC_ROOT = "mimic-iv-2.2" # ← 请替换成你的实际路径
OUTPUT_MD = 'mimic_iv_preview.md'
SUBDIRS = ['hosp', 'icu']
# ==============

def dataframe_to_markdown_table(df, table_name):
    """将 DataFrame 转为规整的 Markdown 表格（含表头和分隔线）"""
    if df.empty:
        return f"### {table_name}\n\n（表格为空）\n\n"
    
    # 替换 NaN 为空字符串以便显示
    df = df.fillna('')
    
    # 构建表头
    headers = df.columns.tolist()
    header_row = '| ' + ' | '.join(headers) + ' |'
    separator_row = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    
    # 构建数据行
    data_rows = []
    for _, row in df.iterrows():
        cells = [str(cell).replace('\n', ' ').replace('|', '\\|') for cell in row]
        data_rows.append('| ' + ' | '.join(cells) + ' |')
    
    md_table = f"### `{table_name}`\n\n{header_row}\n{separator_row}\n" + "\n".join(data_rows) + "\n\n"
    return md_table

def main():
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write("# MIMIC-IV v2.2 数据集预览（每表前5行）\n\n")
        f.write("> 自动生成于: 2026-01-19\n\n")

    for subdir in SUBDIRS:
        dir_path = os.path.join(MIMIC_ROOT, subdir)
        if not os.path.exists(dir_path):
            print(f"⚠️ 跳过不存在的目录: {dir_path}")
            continue

        print(f"📁 正在处理目录: {subdir}")
        csv_files = [f for f in sorted(os.listdir(dir_path)) if f.endswith('.csv.gz')]
        
        if not csv_files:
            continue

        with open(OUTPUT_MD, 'a', encoding='utf-8') as f:
            f.write(f"## `{subdir}/` 目录\n\n")

        for csv_file in csv_files:
            full_path = os.path.join(dir_path, csv_file)
            table_name = f"{subdir}/{csv_file}"
            try:
                # 只读前5行
                df = pd.read_csv(full_path, nrows=5, low_memory=False)
                md_table = dataframe_to_markdown_table(df, table_name)
                
                with open(OUTPUT_MD, 'a', encoding='utf-8') as f:
                    f.write(md_table)
                print(f"  ✅ {csv_file}")
            except Exception as e:
                error_msg = f"### `{table_name}`\n\n❌ 读取失败: {str(e)}\n\n"
                with open(OUTPUT_MD, 'a', encoding='utf-8') as f:
                    f.write(error_msg)
                print(f"  ❌ {csv_file}: {e}")

    print(f"\n✅ 所有预览已保存至: {os.path.abspath(OUTPUT_MD)}")

if __name__ == "__main__":
    main()