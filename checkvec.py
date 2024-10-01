import pandas as pd

# 讀取已保存的 Excel 文件
df = pd.read_excel('Vectorized_延伸我.xlsx')

# 檢查是否有任何空的向量
empty_vectors = df[df['vector'].isnull()]
if empty_vectors.empty:
    print("所有向量均已正確儲存。")
else:
    print("存在空向量，請檢查以下行：")
    print(empty_vectors)

# 確認向量的維度是否正確（假設向量應為 100 維）
df['vector_dim'] = df['vector'].apply(lambda x: len(eval(x)) if isinstance(x, str) else None)
incorrect_dims = df[df['vector_dim'] != 100]
if incorrect_dims.empty:
    print("所有向量的維度均為 100。")
else:
    print("以下行的向量維度不正確：")
    print(incorrect_dims)
