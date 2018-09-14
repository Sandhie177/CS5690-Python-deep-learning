#import numpy modules
import numpy as np
#creating a array having random variables from 1 to 20 in size 15
a=np.random.randint(20,size=(15))
#Counting the number of time each element present in the array
counts = np.bincount(a)
#Print the array
print (a)
#Print the element which present maximum times in the array
print (np.argmax(counts))