# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import nltk

#reading a wiki page
#Get the URl
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
#Put the contents in a variable
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
file  = open('input.txt', 'w') #opening file to write in
#print (para)
for link in soup.find_all('p'):
    
    file.write(str(link.get_text().encode("utf-8")))
    
file.close()
#reading wiki page ends

##tokenization starts
file_content = open("input.txt").read()
wtokens = nltk.word_tokenize(file_content) #word token
stokens = nltk.sent_tokenize(file_content) #sentence token

print ('\nPerfoming tokenization:\n')
print ('sentence tokeniztion:\n')
for s in stokens:
    print (s) #printing tokenized sentence

print ('\nWord tokeniztion:') 
for t in wtokens:
    print (t) #printing tokenized word
##tokenization ends
    
#stemming starts
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

#performing stemming
print ('\nperfoming stemming:')
for w in wtokens:
    pStemmer = PorterStemmer() #porter stemming
    print (pStemmer.stem(w))

    lStemmer = LancasterStemmer() #lancaster stemming
    print (lStemmer.stem(w))

    sStemmer = SnowballStemmer('english') #snowball stemming
    print (sStemmer.stem(w))
#stemming ends
    
#Parts of Speech tagging starts
print ('\nperfoming POS:')
text = nltk.word_tokenize(file_content) 
print (nltk.pos_tag(text)) #performing POS tag
#POS ends

#lemmatization starts  
print ('\nperforming lemmatization:')    
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

for w in wtokens:
    print (lemmatizer.lemmatize(w)) #performing lemmatizer
#lemmatization ends
    
#trigram starts
print ('\nperforming Trigram:')
from nltk import ngrams

n = 3 #n defines the number of ngrams
trigrams = ngrams(file_content.split(), n) #splitting with respect to n
for grams in trigrams:
  print (grams)
#trigram ends
  
#Named Entity Recognizer starts
print ('\nPerforming NER:')

from nltk import word_tokenize, pos_tag, ne_chunk

print (ne_chunk(pos_tag(word_tokenize(file_content))))
#NER ends