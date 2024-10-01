from ckip_transformers.nlp import CkipWordSegmenter

# 初始化 CKIP 的分詞器
ws_driver = CkipWordSegmenter()

# 輸入需要斷詞的句子
sentence_list = ["我是一個21歲的台灣男性大學生。"]

# 執行斷詞
word_splitted_sentence = ws_driver(sentence_list)

# 顯示結果
for sentence in word_splitted_sentence:
    print(sentence)
