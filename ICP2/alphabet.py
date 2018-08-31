
#3rd problem of ICP2
#this code will display Z
def display(n):
 
    for i in range(n):
 #outer loop for print
        for j in range(n):
 #inner loop for print
            if (i == 0 or i == n-1) or i==n-j-1: #print * at the first and last row and also a diagonal line
                print("*", end = "")
            else:
                print(" ", end = "")
         
        print()
     
display(10)
