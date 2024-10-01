import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# 1. 讀取 Excel 檔案
file_path = 'Vectorized_延伸人.xlsx'  # 替換為你的檔案路徑
df = pd.read_excel(file_path)

# 2. 確保向量是列表格式，如果向量是字串，則使用 eval() 轉換
df['vector'] = df['vector'].apply(eval)

# 3. 將向量轉換為 numpy array
vectors = np.array(df['vector'].tolist())

# 4. 使用 t-SNE 將高維向量降到 2D 空間
tsne = TSNE(n_components=2, random_state=0)
vectors_2d = tsne.fit_transform(vectors)

# 5. 繪製 t-SNE 結果
plt.figure(figsize=(10, 7))

# 繪製所有向量的 2D 分佈
plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], c='blue', label='課程向量', edgecolor='black')

# 添加課程名稱作為標籤
for i, txt in enumerate(df['課程名稱']):
    plt.annotate(txt, (vectors_2d[i, 0], vectors_2d[i, 1]))

plt.title('課程向量的 t-SNE 視覺化')
plt.legend()
plt.show()
