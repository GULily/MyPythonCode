# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#conda install gensim
#conda install -c anaconda nltk=3.2.1
#Download stopwords from nltk library
#>>import nltk
#>>> nltk.download()
#in NLTK Donwloader select following:
#1. go to corpora
#2. within corpora select stopwords
#3. click download

##########write limitations in the end#######
#### the questions ####
#### 10 rows of data set ####
#### one paragragh overall of project 1 ####
### story begins (viisualization + conclusion) ####

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models, similarities
import numpy as np

tokenizer = RegexpTokenizer('\s+', gaps=True) # tokenize
en_stop = stopwords.words('english') # create English stop words list
# add more words to the stop list
more_stopwords = """terminated ongoing inc llc lp firm company product products recall recalling recalled food foods may due use uses used fda lot & 1 24 2012 2013 2014 2015 2016"""
en_stop += more_stopwords.split()
#print(en_stop)
p_stemmer = PorterStemmer() # stem
    
# Here we consider each record in the file as one document, 
# so there are thousands of documents in this file.
f=open("word_frequency.csv", "r", encoding="latin1")
np.random.seed(7) # set random seed (results are unstable)

texts = [] # list for tokenized documents in loop
# loop through each line of the file
for i in f:    
    raw = i.lower() # clean and tokenize document string
    raw = raw.replace(',',' ')
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop] # remove stop words from tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens] # stem tokens
    texts.append(stemmed_tokens) # add tokens to list
# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
# generate LDA model
ldamodel = models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
topics = ldamodel.print_topics(num_topics=6, num_words=15)

print('\n\n', str(f.name))
# change the format of output results to make them clear    
for line in topics:
    print("\nTopic", line[0])
    words = line[1].rstrip().split(' + ')  # remove the trailing '\n'
    for i in range(len(words)):
        print(words[i])
        
        
# topic distributions of one example 
print("Example: Positive sample shows that listeria monocytogenes contaminate ice cream.")
print("  Topic distributions of the example:")
print(ldamodel[dictionary.doc2bow(['positive','sample','show','that','listeria', 'monocytogenes', 'contaminate','ice', 'cream'])])



# similiarity of text
# top ten records similiar to the example 
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=8)
doc = "Positive sample shows that listeria monocytogenes contaminate ice cream."
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # convert the query to LSI space
index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
sims = index[vec_lsi] # perform a similarity query against the corpus
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print("  Top 10 records similar to the example:")
print(sims[0:9]) # print sorted (document number, similarity score) 2-tuples



