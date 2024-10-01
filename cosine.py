import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

# 1. 讀取課程和 CEEC 向量資料
keywords_df = pd.read_excel('Vectorized_延伸物.xlsx')  # 讀取關鍵詞資料
ceec_vector = pd.read_excel('CEEC向量.xlsx')  # 讀取 CEEC 向量資料

# 2. 將課程向量和 CEEC 向量的 'vector' 欄位轉換為數值格式
keywords_df['vector'] = keywords_df['vector'].apply(eval)
ceec_vector['vector'] = ceec_vector['vector'].apply(eval)

# 3. 將這些向量轉換為 numpy 陣列，方便進行相似度計算
course_vectors_cleaned = np.array(keywords_df['vector'].tolist())
ceec_vectors = np.array(ceec_vector['vector'].tolist())

# 4. 計算每個課程向量與每個 CEEC 向量之間的餘弦相似度
similarities_cleaned = cosine_similarity(course_vectors_cleaned, ceec_vectors)

# 5. 找出每個課程最相似的 CEEC 類型
most_similar_ceec_indices_cleaned = np.argmax(similarities_cleaned, axis=1)
most_similar_ceec_categories_cleaned = ceec_vector['CEEC類型'].iloc[most_similar_ceec_indices_cleaned].values

# 6. 建立一個 DataFrame 來顯示課程名稱、最相似的 CEEC 類型以及相似度分數
similarity_results_cleaned = pd.DataFrame({
    '課程名稱': keywords_df['課程名稱'],
    '最相似的CEEC類型': most_similar_ceec_categories_cleaned,
    '相似度': similarities_cleaned[np.arange(len(keywords_df)), most_similar_ceec_indices_cleaned]
})

# 7. 顯示結果或保存到 Excel
similarity_results_cleaned.to_excel("CEEC延伸物.xlsx", index=False)
