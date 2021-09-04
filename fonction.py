def countwordsfromfile() :
    fileName=input("enter a sentence")
    numberofwords=0
    file=open(fileName,"r")
    for line in file:
        words=line.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)
countwordsfromfile()


