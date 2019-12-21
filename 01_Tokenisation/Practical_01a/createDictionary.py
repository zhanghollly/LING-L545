# -*- coding: utf-8 -*-
#!/usr/local/bin/python3
from conllu import parse_incr
import codecs

def createDictionary(tokenDict, out_file):
    """dictionary, string -> void"""
    #given a dictionary of tokens and a filename, creates a file with one token per line
    with codecs.open(out_file, 'w', encoding='utf8') as file:
        #get each token
        for token in tokenDict:
            file.write(token+"\n")
    file.close()


def readFile(filename):
    """string -> dictionary"""
    #takes a file name and returns a dictionary of all the tokens as keys
    tokenDict = dict()
    with codecs.open(filename, 'r', encoding='utf8') as file:
        #get the tokens in each sentence
        for tokenlist in parse_incr(file):
            #get each individual token
            for token in tokenlist:
                #add the token to the dictionary with an arbitrary value
                tokenDict[token["form"]] = 1
    file.close()
    return tokenDict


def main():
    #create the dictionary file from the training set
    tokenDict = readFile("UD_Japanese-GSD/ja_gsd-ud-train.conllu")
    createDictionary(tokenDict, "tokenDictionary.txt")

    #create the file from the testing set for comparing maxmatch
    testingDict = readFile("UD_Japanese-GSD/ja_gsd-ud-test.conllu")
    createDictionary(testingDict, "testingTokens.txt")

main()
