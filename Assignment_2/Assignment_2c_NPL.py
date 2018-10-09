#Write a programinwhich take an Input file. 
#Use the simple approach below to summarize a text file:
#a. Read afile b. Apply lemmatization on the words
#c. Apply the bigram on the text
#d. Calculate the word frequency (bi-gram frequency) of the words (bi-grams)
#e. Choose top five bi-grams that have been repeated most
#f. Go through the original text that you had in the file
#g. Find all the sentences with those most repeated bi-grams
#h. Extract those sentences and concatenate

#importing libraries
import re
import nltk

##reading a file
print ('\na) reading a file')
file_content = open("big.txt").read()
print (file_content)
words = nltk.word_tokenize(file_content) #tokennizing

print ('\nb) performing lemmatization:')    
#importing libraries
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() #lemmatization

for w in words:
    print (lemmatizer.lemmatize(w)) 

#bigram starts   
print ('\nc) performing Bigram:')
#importing libraries
from nltk import ngrams

n = 2 #n defines the number of ngrams
bigrams = ngrams(file_content.split(), n) #splitting with respect to n
for grams in bigrams: #loop to create bigrams
  print (grams)

#calculating word frequency
print ('\nd) Calculating Word frequency')
#importing libraries
from itertools import islice
from collections import Counter

all_count = Counter(zip(words, islice(words, 1, None))) #using counter function to count the bigrams

print (all_count)

#finding the top five bigrams that have been repeated most

print ('\ne) Finding top 5 bigrams according to repeatation: ')
most_common = all_count.most_common(5) #using most_common operation to find most repeated bigrams
print (most_common)
a = []
for i in range(0,(len(most_common))): #loop to form a list of most common bigrams
    b=most_common[i]
    a.append (b[0]) 

#going through the original text file
print ('\nf) going through original text file')
with open('big.txt') as f:
    content = f.readlines()

#finding all the sentences with most repeated bigrams
print ('\ng) finding all the sentences with most repeated bigrams and concatenate')
lines = content[0].split('.') #splitting the lines in the original files
match = ""; #creating empty string
for j in range(0,len(a)): #loop to take the elements in the bigram
    q = a[j]
    p = q[0] + ' ' + q[1] #taking two words which constitute a bigram
    for i in range(0,len(lines)): #loop to match the bigrams inside the line
        if p in lines[i]:
            match += (lines[i]) + '. ' #if matches, take the sentence in a string

print (match)

