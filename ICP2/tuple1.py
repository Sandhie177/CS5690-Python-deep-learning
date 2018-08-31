# -*- coding: utf-8 -*-
#1st problem of ICP2

n=eval(input("How many numbers do you have?"))
i=0
list1=[] #creating an empty list
for i in range(n):
    x=int(input("enter a number"))
    list1.append(x) #appending the numbers to the blank list
print("the list is",list1)
a=list1[0] #finding the first element of the list
b=list1[n-1] #finding the last element of the list
tuple1=(a,b) #creating the tuple
print ("the tuple is", tuple1) 

