#Suppose you have two files. And what is inside the files are as follows:
#File1:“This time, we are going to learn how to write programs that recognize objects in
# images using deep learning. In other words, weare going to explain the black magic 
#that allows Google Photos to search your photos based on what is in the picture”
#File2:“this we to are in the that your on based what is how other”
#Program a code such that you remove everything in the File1which is insideFile2.

import re
# opening two files for reading
f1 = open('file1.txt', 'r') 
f2 = open('file2.txt', 'r')
# opening file for writing
f3 = open('output.txt', 'w')

#copying the datas of the file in another file
file1_raw = f1.read()
file2_raw = f2.read()
#splitting the words in terms of " "
match1 = re.findall(r'(\w+\S)',str(file1_raw))
match2 = re.findall(r'(\w+\S)',str(file2_raw))
#print (match1)
#print (match2)
#matches word by word within two files and keeps the non matching words in l3
l3= [word for word in match1 if word.casefold() not in match2]

#writes each letter of l3 in output file
for word in l3:          
    f3.write("%s " %(word))
    #closes the output file
f3.close()

        
