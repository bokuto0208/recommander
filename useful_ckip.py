import pandas as pd
from ckip_transformers.nlp import CkipWordSegmenter

# 1. 讀取 Excel 文件
file_path = 'Cleaned_延伸人.xlsx'  # 替換為你的本地檔案路徑
df = pd.read_excel(file_path)

# 2. 初始化 CKIP 分詞器
ws_driver = CkipWordSegmenter()

# 3. 定義 CKIP 分詞函數
def ckip_word_segmentation(text):
    if isinstance(text, str):
        return ws_driver([text])[0]  # 使用 CKIP 分詞
    return []

# 4. 對處理過的文本進行分詞
df['keywords'] = df['processed_text'].apply(ckip_word_segmentation)

# 5. 刪除 processed_text 欄位
df = df.drop(columns=['processed_text'])

# 6. 保存處理後的資料為新的 Excel 檔案
output_file = 'Segmented_Cleaned_延伸人.xlsx'
df.to_excel(output_file, index=False)

# 或者保存為 CSV 檔案
# output_file = 'Segmented_Cleaned_延伸物.csv'
# df.to_csv(output_file, index=False)

print(f"分詞結果已經保存到: {output_file}")
