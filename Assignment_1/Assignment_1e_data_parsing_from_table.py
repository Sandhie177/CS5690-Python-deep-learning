# program a code which download a webpage contains a table using Request library, then parse the page using 
#Beautifusoup library. You should save all the information of the table in a file.

#importing libraries 
#"BeautifulSoup" for data parsing
#"urllib" for importing the html file from a url link
#"re" for regexp operation
from bs4 import BeautifulSoup
import urllib.request
import re

#Get the URl
url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"
#Put the contents in a variable
source_code = urllib.request.urlopen(url)
plain_text = source_code

#Calling the BeatifulSoup library for data parsing 
soup = BeautifulSoup(plain_text, "html.parser")

#print (soup.find_all('tr'))
table_file  = open('web_table.txt', 'w') 
#Getting table data for each tr tag which represents rows
for link in soup.find_all('tr'):
    
    #extracting all table header using regexp operation matching the pattern
    match = re.findall(r'\">(\S+)<\/th',str(link))
    #extracting all column elements with numbers using regexp operation matching the pattern
    match1 = re.findall(r'\">(\S+)<\/td',str(link))
    #extracting column elements containing player name which has links using regexp operation matching the pattern
    match2 = re.findall(r'\">(\S+\s\w+)\<\/a',str(link))
    #extracting column elements containing team name which has links using regexp operation matching the pattern
    match3 = re.findall(r'\">(\w+)</a',str(link))
    #extracting columns elements which doesn't contain player name
    match4 = re.search(r'></a',str(link))
    
    #if finds the header writes all the header names in file with mentioned column widths
    if (match):
        table_file.write('{:^4} {:^20} {:^4} {:^5} {:^5} {:^4}\n'.format(*match))
    #if find all the elements in the row, writes all the column elements in a row in file with mentioned column widths
    if (match1) and (match2) and (match3):
        table_file.write('{:^4} {:<20} {:<4} {:^5} {:^5} {:^4}\n' .format(match1[0], match2[0], match3[0],match1[2],match1[3],match1[4]))
    #if find all the elements in the row along with blank player name and team, writes all the column elements 
    #in a row in file with mentioned column widths
    if (match1) and (match4):
        table_file.write('{:^4} {:<20} {:<4} {:^5} {:^5} {:^4}\n' .format(match1[0], "", "",match1[3],match1[4],match1[5]))
#closes file
table_file.close()