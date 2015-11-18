import gensim
from dta import *

BASE_DIR = "../../data/koppel" # NOTE: Update BASE_DIR to your own directory path
model_download_path = "blog_posts_300_c_40.word2vec"
model = gensim.models.Word2Vec.load(model_download_path)


import graphlab as gl
sframe_save_path = "blogs.sframe"
sf = gl.load_sframe(sframe_save_path)
print sf.num_rows()


# first we join the posts list to a single string
sf['posts'] = sf['posts'].apply(lambda posts:"\n".join(posts))

# Construct Bag-of-Words model and evaluate it
sf['1gram features'] = gl.text_analytics.count_ngrams(sf['posts'], 1)
sf['2gram features'] = gl.text_analytics.count_ngrams(sf['posts'], 2)

dt = DeepTextAnalyzer(model)
sf['vectors'] = sf['posts'].apply(lambda p: dt.txt2avg_vector(p, is_html=True))
#print sf['vectors'].head(1)
sf = sf.dropna()

print "Spliting data."

train_set, test_set = sf.random_split(0.8, seed=5)

print "Predicting Gender"

cls = gl.classifier.create(train_set, target='gender', features=['1gram features'])
baseline_result = cls.evaluate(test_set)
print baseline_result

