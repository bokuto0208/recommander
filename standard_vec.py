import pandas as pd
from gensim.models import Word2Vec

# 1. 讀取經過分詞處理的 XLSX 文件
file_path = 'ceec格式化.xlsx'  # 替換為你的 XLSX 檔案路徑
df = pd.read_excel(file_path)  # 使用 read_excel 來讀取 XLSX 文件

# 2. 確保 'keywords' 欄位是列表格式，加入錯誤處理
def safe_eval(x):
    try:
        return eval(x)
    except:
        return []

df['keywords'] = df['keywords'].apply(safe_eval)

# 3. 使用 Word2Vec 訓練模型
# 'vector_size' 可以設定向量的維度，這裡設定為 100 維
model = Word2Vec(df['keywords'], vector_size=100, window=5, min_count=1, workers=4)

# 4. 將每個 MBTI 類型的詞嵌入向量計算出來，並轉換為逗號分隔、並用[]括起來的字串
def text_to_vector(tokens):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    if vectors:
        avg_vector = sum(vectors) / len(vectors)  # 計算詞向量的平均值
        return '[' + ','.join(map(str, avg_vector)) + ']'  # 將向量轉為逗號分隔並用[]括起來
    else:
        return '[' + ','.join(['0'] * 100) + ']'  # 若詞不在模型中，返回 100 維零向量並用[]括起來

df['vector'] = df['keywords'].apply(text_to_vector)

# 5. 保存向量化的結果到一個新的 Excel 檔案
output_file = 'CEEC向量.xlsx'
df[['CEEC類型', 'vector']].to_excel(output_file, index=False)  # 使用 to_excel 保存為 Excel

print(f"向量化結果已保存到: {output_file}")
