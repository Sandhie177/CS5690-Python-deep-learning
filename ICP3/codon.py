
import csv #imoprting library
i=1
while i%3 !=0:
    string=input('Give the sequence of DNA:')
    i=len(string)
    if i%3 !=0:
        print ('Sequence is invalid. Give the Sequence Again') #if there is a sequence 
                                                               #with 1 or 2 characters it can't process

list1=[] #creating empty list
dict1={}
for x in range(i):
    if x%3==0:
        list1.append(string[x:x+3]) #spliting the string by 3 elements and keeping them in list1
for x in range(len(list1)):       
    with open('codon.tsv') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
          if list1[x] in row:
              if row[1] in dict1:
                  dict1[row[1]] +=1 #counts the number of each codon sequense
              else: 
                  dict1[row[1]] =1
                    
print (dict1)                





#list1=[i for i in string]
#print (list(list1))