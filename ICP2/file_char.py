
#2nd problem of ICP2
fileName= input("What  file are the words  in? ")
infile= open(fileName,'r') #opening the file for reading

word_count=1 #initializing the count
char_count=0 #initializing the count
line = infile.readline() #reading line
while line != "":
    if line[len(line)-1]== "\n": #if end of line reaches it will ignore the \n
        p= len(line)-1
        text = line [0:len(line)-1]
    else:
        p=len(line)
        text = line
    for i in range(p):
        if line[i] == " ": #if space is found in a line it will take it as a new word
            word_count +=1
        if line[i] != " ":
            char_count +=1
    print ("%s %d,%d" %(text, word_count, char_count))
    line = infile.readline()
    word_count=1
    char_count=0