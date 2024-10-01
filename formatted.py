import pandas as pd

# 1. 讀取 Excel 檔案
file_path = 'mbti.xlsx'  # 替換為你的檔案路徑
df = pd.read_excel(file_path)

# 2. 合併需要合併的欄位內容到 'keywords'
# 假設你要合併 'Unnamed' 開頭的所有欄位，但排除 'CEEC類型' 和現有的 'keywords'
columns_to_merge = [col for col in df.columns if col != 'MBTI類型' and col != 'keyword']  # 排除不需要的欄位

# 合併欄位內容，並將合併結果放到 'keywords' 中
df['keywords'] = df[columns_to_merge].apply(lambda row: ' '.join(row.dropna().astype(str)), axis=1)

# 3. 定義一個函數來將合併後的 'keywords' 轉換為標準的 Python 列表格式
def format_keywords(keywords):
    # 將關鍵字用空格分隔為列表
    keywords_list = keywords.split()  # 假設關鍵字是用空格分隔的
    # 將每個關鍵字包裹在引號中，並以逗號分隔
    formatted_list = [f"'{word}'" for word in keywords_list]
    return f"[{', '.join(formatted_list)}]"

# 4. 將 'keywords' 欄位的內容轉換為標準的 Python 列表格式
df['keywords'] = df['keywords'].apply(format_keywords)

# 5. 保留 'CEEC類型' 和新的 'keywords' 欄位
df_cleaned = df[['MBTI類型', 'keywords']]

# 6. 保存處理後的結果為新的 Excel 檔案
output_file = 'mbti格式化.xlsx'
df_cleaned.to_excel(output_file, index=False)

print(f"結果已保存到: {output_file}")
