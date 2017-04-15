from gensim.models import word2vec

sentences = word2vec.Text8Corpus("data/sentences.txt")
model = word2vec.Word2Vec(sentences, size=200)


model.most_similar(['man'])

# clustering