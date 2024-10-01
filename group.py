import pandas as pd

# 讀取 Excel 檔案
file_path = 'ceec.xlsx'  # 替換為你的檔案路徑
df = pd.read_excel(file_path)

# 檢查欄位名稱
print(df.columns)

# 2. 合併 'Unnamed' 開頭的欄位內容到 'keywords'，但不包括 'CEEC類型' 和 'keywords'
columns_to_merge = [col for col in df.columns if col != 'CEEC類型' and col != 'keywords']  # 排除 'CEEC類型' 和 'keywords'
df['keywords'] = df[columns_to_merge].apply(lambda row: ' '.join(row.dropna().astype(str)), axis=1)

# 3. 保留 'CEEC類型' 和 'keywords' 欄位
df_cleaned = df[['CEEC類型', 'keywords']]

# 4. 保存結果為 Excel 檔案
output_file = 'Formatted_CEEC_Data.xlsx'
df_cleaned.to_excel(output_file, index=False)

print(f"結果已保存到: {output_file}")
