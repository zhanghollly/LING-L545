import codecs
import sys
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
    """string, dictionary -> boolean"""
    if dictionary.get(firstword, "Not in the dict") != "Not in the dict":
        return true
    return false

def readTokenDict(filename):
    """string -> dictionary"""
    #read the token dictionary written in a file and create a dictionary in python
    tokenDict = dict()
    with codecs.open(filename, 'r', encoding='utf8') as file:
        #get each token and add it to the dictionary as a key
        for line in file:
            token = line.strip('\n')
            tokenDict[token] = 1
    file.close()
    return tokenDict


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise Exception('Please provide three commandline arguments.')
    (dictionary_file, sentence) = sys.argv[1:]

    #create the token dictionary
    tokenDict = readTokenDict(dictionary_file)

    #get tokens from the sentence using maxmatch and display them
    predictedTokens = maxmatch(sentence, tokenDict)
    for pt in predictedTokens:
        print(pt)

##    logics = { "human" : human_IJK.next_move, "ai" : ai_IJK.next_move }
##    deterministic = { "det" : True, "nondet" : False }

##    IJK(logics[p1], logics[p2], deterministic[mode])
