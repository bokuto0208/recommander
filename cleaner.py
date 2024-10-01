import re

def clean_text(text):
    # 移除多餘的空格、換行符號等
    text = re.sub(r'\s+', ' ', text)
    # 移除特殊字符等
    text = re.sub(r'[^\w\s]', '', text)
    return text

df['processed_text'] = df['課程名稱'] + ' ' + df['課程教學目標'] + ' ' + df['課程綱要及進度']
df['processed_text'] = df['processed_text'].apply(clean_text)

# 查看清理後的數據
df[['課程名稱', 'processed_text']].head()
