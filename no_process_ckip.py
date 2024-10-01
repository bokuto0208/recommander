import pandas as pd
import re
from ckip_transformers.nlp import CkipWordSegmenter

# 1. 讀取 Excel 文件
file_path = '延伸物.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 2. 定義清理文本的函數
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'\s+', ' ', text)  # 移除多餘空格、換行符號
        text = re.sub(r'[^\w\s]', '', text)  # 移除特殊字符
        return text
    return text

# 3. 將課程名稱、教學目標和課程綱要進行合併並清理
df['processed_text'] = df['課程名稱'] + ' ' + df['課程教學目標'] + ' ' + df['課程綱要及進度']
df['processed_text'] = df['processed_text'].apply(clean_text)

# 4. 初始化 CKIP 分詞器
ws_driver = CkipWordSegmenter()

# 5. 定義 CKIP 分詞函數
def ckip_word_segmentation(text):
    if isinstance(text, str):
        return ws_driver([text])[0]  # 使用 CKIP 分詞
    return []

# 6. 對處理過的文本進行分詞
df['keywords'] = df['processed_text'].apply(ckip_word_segmentation)

# 7. 保存處理後的資料為新的 Excel 檔案
output_file = 'processed_data.xlsx'
df.to_excel(output_file, index=False)

# 或者保存為 CSV 檔案
# output_file = 'processed_data.csv'
# df.to_csv(output_file, index=False)
