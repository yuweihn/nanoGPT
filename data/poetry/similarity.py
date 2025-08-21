from gensim.models import Word2Vec

sentences = [
    ["机器学习", "很", "有趣"],
    ["让", "我们", "一起", "学习"],
    ["机器学习", "是", "人工智能", "的", "一个", "分支"]
]

# 训练Word2Vec模型
model = Word2Vec(sentences, vector_size=50, window=2, min_count=1, workers=4)

# 获取词向量
word_vector_ml = model.wv['机器学习']
word_vector_ai = model.wv['人工智能']

print("机器学习的词向量：", word_vector_ml)
print("人工智能的词向量：", word_vector_ai)

# 计算词向量之间的相似度
similarity = model.wv.similarity('机器学习', '人工智能')
print("机器学习与人工智能的相似度：", similarity)
