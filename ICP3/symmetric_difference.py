# -*- coding: utf-8 -*-
#A={1,2,3,4}
#B={1,2}
def list1():
    n=eval(input("How many numbers do you have in the list?")) #takes number of elements in the list
    i=0
    list1={0} #creating an empty set
    list1.remove(0)
    for i in range(n):
        x=int(input("enter a number\n"))
        list1.add(x) #adding new numbers to the list
    
    print("the list is",list1) #prints the list
    return list1 #returns the list
A=list1() #calls the function list1 to take input list A
B=list1() #calls the function list1 to take input list B

print ("the symmetric difference between set A and B is:", A^B)

