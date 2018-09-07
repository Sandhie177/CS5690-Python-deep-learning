# -*- coding: utf-8 -*-


#importing libraries
from bs4 import BeautifulSoup
import urllib.request
import os

#Get the URl
url = "https://en.wikipedia.org/wiki/Deep_learning"
#Put the contents in a variable
source_code = urllib.request.urlopen(url)
plain_text = source_code

#Calling the BeatifulSoup library for data parsing 
soup = BeautifulSoup(plain_text, "html.parser")

#Printing the header of the file
print (soup.title.string)

#creating a empty list
href_list = []

#Getting href for each a tag
for link in soup.find_all('a'):
    #print(link.get('href'))
    href_list.append(link.get('href'))
    #if (link.get('href').startswith("http")):
    #        href_list.append(link.get('href'))
#Printing href    
for link in href_list:
    print(link)