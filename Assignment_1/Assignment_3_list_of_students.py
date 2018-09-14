#function to create list
def list1():
    n=eval(input("Student number:")) #takes number of elements in the list
    i=0
    list1=[] #creating an empty set
    #list1.remove(0)
    for i in range(n):
        x=str(input("enter name\n"))
        list1.append(x) #adding new members to the list
    
    print("the list of student is",list1) #prints the list
    return list1 #returns the list
#creating function to find out the difference
def Diff(li1, li2): 
    #converting the list into set and substracting
    return (list(set(li1) - set(li2))) 
#creating python database
print ("For python class,") #mentioning the name of class
python=list1() #calls the function list1 to take input for python class
#creating web_application database
print ("\n For web application class,") #mentioning the name of class
web_app=list1() #calls the function list1 to take input for web application class
d = (Diff(python, web_app))
print ("the list of students who are taking python but not web application is:", d)