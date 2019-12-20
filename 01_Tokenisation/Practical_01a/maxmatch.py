#maxmatch algorithm

def maxmatch(sentence, dictionary):
    if sentence == "":
        return []
    for i in range(len(sentence), 1, -1):
        firstword = sentence[0 : i]
        remainder = sentence[i :]
        if inDict(firstword, dictionary):
            return list(firstword, maxmatch(remainder, dictionary))
    firstword = sentence[0]
    remainder = sentence[1:]
    return list(firstword, maxmatch(remainder, dictionary))

def inDict(firstword, dictionary):
    return "blah"
    #read the token dictionary written in a file

def createDict(in_file, out_file):
    return "blah"
    #reads each line of in_file
    #calls tokenise to tokenize each sentence
    #writes the new tokens into outfile

def tokenise():
    return "blah"
    #tokenise each sentence

def wordErrorRate():


def main():

