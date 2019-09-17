#maxmatch algorithm

def maxmatch(sentence, dictionary):
    if sentence == "":
        return []
    for i in range(len(sentence), 1, -1):
        firstword = sentence[0 : i]
        remainder = sentence[i : -1]
        if inDict(firstword, dictionary):
            return list(firstword, maxmatch(remainder, dictionary))

def inDict(firstword, dictionary):
    #read the token dictionary written in a file

def createDict(in_file, out_file):
    #reads each line of in_file
    #calls tokenise to tokenize each sentence
    #writes the new tokens into outfile

def tokenise():
    #tokenise each sentence
