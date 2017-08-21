# basic settings
from gensim import corpora
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora, models
import pyLDAvis
import pyLDAvis.gensim
from pprint import pprint
import logging
import string
import os


#print os.getcwd()
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#document = open("allReviews.csv").read()

## pre-processing
tokens = []
for line in open('allReviews.csv'):
    texts = [text for text in line.lower().split() if text not in STOPWORDS]
    texts = [text.translate(None, string.punctuation) for text in texts]
    texts = [text for text in texts if not text.isdigit()]
    texts = [text for text in texts if len(text) > 1]
    if (texts != []):
        tokens.append(texts)

## build topic model
dictionary = corpora.Dictionary(tokens)
corpus = [dictionary.doc2bow(token) for token in tokens]
lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, passes=10, eval_every=None)
lda.print_topics(10)

## visualization
vis_data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.display(vis_data)
pyLDAvis.save_html(vis_data, 'ldavis.html')