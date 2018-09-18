#search in a string and find the first non-repeated characters in that string
#Input:Deep data structure
#Output: p

#taking the list as input
string = input('Write down the line:')
count = 0 #initializing count

for i in range(len(string)): #1st loop to get the 1st letter
    for j in range(len(string)): #2nd loop to match with rest of the letters
        if string[i] != string[j]:
            count +=1 #checks if the 1st letter matches with any other letter
    if count == len(string)-1: #if any letter is used only once
        print (string[i]) #prints that letter
        break
    count = 0 #makes count 0 for next loop