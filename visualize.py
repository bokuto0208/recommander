import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# 1. 讀取 CEEC 向量資料
ceec_file_path = 'CEEC向量.xlsx'  # 替換為你的檔案路徑
df_ceec = pd.read_excel(ceec_file_path)

# 2. 將向量從字串轉換為 Python 列表
df_ceec['vector'] = df_ceec['vector'].apply(eval)

# 3. 將向量轉換為 numpy array
ceec_vectors = np.array(df_ceec['vector'].tolist())

# 4. 使用 t-SNE 將高維的向量降到 2D
tsne = TSNE(n_components=2, random_state=0)
ceec_vectors_2d = tsne.fit_transform(ceec_vectors)

# 5. 繪製 t-SNE 結果
plt.figure(figsize=(10, 7))

# 繪製每個 CEEC 類別的向量，使用不同顏色標記
plt.scatter(ceec_vectors_2d[:, 0], ceec_vectors_2d[:, 1], c='red', label='CEEC類型', edgecolor='black')

# 添加 CEEC 類型的標籤
for i, txt in enumerate(df_ceec['CEEC類型']):
    plt.annotate(txt, (ceec_vectors_2d[i, 0], ceec_vectors_2d[i, 1]))

plt.title('CEEC 向量的 t-SNE 視覺化')
plt.legend()
plt.show()
