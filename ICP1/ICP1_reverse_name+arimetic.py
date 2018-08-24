# -*- coding: utf-8 -*-

#function to invert the name
def invert(name):
    j=len(name)
    j=j-1
    name1=[]
    while j>-1:
        name1.append(name[j])
        j=j-1
    return name1
First=input ('Please enter first name: ')
Second=input ('Please enter second name: ')

a=invert(Second) #calling the function to invert first name
a=''.join(a)
b=invert (First) #calling the function to invert second name
b=''.join(b)


print('\nName is', b, a)

numstring1=input ('Please insert an integer: ')
numstring2=input ('Please insert 2nd integer: ')

num1=int (numstring1)
num2=int (numstring2)
b=num1+num2 #summation
c=abs(num1-num2) #differentiation
d=num1*num2 #multiply
e=num1/num2 #division

print ('\nThe sum of',num1, 'and', num2, 'is' ,b)
print ('The difference between',num1, 'and', num2, 'is' ,c)
print ('The mutiplication of',num1, 'and', num2, 'is' ,d)
print ('The division of',num1, 'and', num2, 'is' ,e)