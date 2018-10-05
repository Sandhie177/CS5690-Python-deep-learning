# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re
import nltk

#Get the URl
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
#Put the contents in a variable
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
#print (soup)
para = soup.find_all('p')
#print (body)
for link in para:
    line = link.get_text()
    print (line)
    

def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())

WORDS = tokens(open('big.txt').read())
##tokenization
file_content = open("big.txt").read()
wtokens = nltk.word_tokenize(file_content)
stokens = nltk.sent_tokenize(file_content)

print ('\nPerfoming tokenization:\n')
for s in stokens:
    print (s)

print ('\n') 
for t in wtokens:
    print (t)

#stemming
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

#performing stemming
print ('\nperfoming stemming:')
for w in wtokens:
    pStemmer = PorterStemmer()
    print (pStemmer.stem(w))

    lStemmer = LancasterStemmer()
    print (lStemmer.stem(w))

    sStemmer = SnowballStemmer('english')
    print (sStemmer.stem(w))

#Parts of Speech tagging
print ('\nperfoming POS:')
text = nltk.word_tokenize(file_content)
print (nltk.pos_tag(text))

#lemmatization   
print ('\nperforming lemmatization:')    
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

for w in wtokens:
    print (lemmatizer.lemmatize(w)) 

#trigram
print ('\nperforming Trigram:')
from nltk import ngrams

n = 3
trigrams = ngrams(file_content.split(), n)
for grams in trigrams:
  print (grams)

#Named Entity Recognizer
print ('\nPerforming NER:')

from nltk import word_tokenize, pos_tag, ne_chunk
 
print (ne_chunk(pos_tag(word_tokenize(file_content))))
