import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import ast

# 讀取分詞後的Excel檔案
segmented_df = pd.read_excel('Segmented_Cleaned_延伸物.xlsx')

# 將關鍵字欄位中的字串轉換為列表
segmented_df['keywords'] = segmented_df['keywords'].apply(ast.literal_eval)

# 將每個課程的關鍵字列表合併成一個字串
segmented_df['joined_keywords'] = segmented_df['keywords'].apply(lambda x: " ".join(x))

# 初始化 TF-IDF Vectorizer，過濾掉常見的停用詞
tfidf_vectorizer = TfidfVectorizer(max_df=0.85, stop_words=[
    ' ', '的', '是', '與', '本', '這', '我', '你', '他', '她', '它', '我們', '你們', '他們', '她們', '這個', '那個', 
    '什麼', '沒有', '可以', '為了', '並且', '但是', '因為', '所以', '而且', '以及', '或者', '如果', '就是', '還有', 
    '而', '了', '在', '與', '和', '呢', '啊', '嘛', '喔', '呀', '的話', '一個', '一些', '所有', '並', '而', '與', '及', 
    '則', '於', '對', '將', '等', '等於', '與其', '例如', '此外', '更', '再次', '尤其', '一樣', '同樣', '這樣', '那樣', 
    '幾乎', '幾個', '個', '些', '更', '比較', '一些', '此外', '雖然', '因此', '隨著', '但是', '已經', '還', '同時'
])

# 訓練 TF-IDF 模型，計算每個關鍵字的權重
tfidf_matrix = tfidf_vectorizer.fit_transform(segmented_df['joined_keywords'])

# 提取出關鍵字的名稱
feature_names = tfidf_vectorizer.get_feature_names()

# 將 TF-IDF 矩陣轉換為 DataFrame 以便處理
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# 將課程名稱加入資料框
tfidf_df['課程名稱'] = segmented_df['課程名稱']

# 提取每個課程中前5個關鍵詞
top_n = 50  # 要提取的關鍵詞數量

# 為每個課程提取最高權重的關鍵詞
top_keywords_df = pd.DataFrame({
    '課程名稱': segmented_df['課程名稱'],
    'Top_Keywords': tfidf_df.drop(columns=['課程名稱']).apply(
        lambda row: row.nlargest(top_n).index.tolist(), axis=1
    )
})

# 將關鍵詞列表轉換為字串形式，方便閱讀
top_keywords_df['Top_Keywords'] = top_keywords_df['Top_Keywords'].apply(lambda x: ', '.join(x))

# 將結果保存為Excel檔案
top_keywords_df.to_excel('keyword_延伸物.xlsx', index=False)

print("關鍵詞提取完成")
