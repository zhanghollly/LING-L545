Holly Zhang (zhanghol)

LING-L545

Practical 01: Tokenisation


### Instructions

#### Creating the Dictionary and Test Files

The dictionary file, currently named "tokenDictionary.txt", is created by running the code below. The "testingTokens.txt" file holds the testing sentences and their tokens from `UD_Japanese-GSD/ja_gsd-ud-test.conllu`. It is also created when the code below is executed. 

`python ./createDictionary.py`


#### Running MaxMatch/Tokenisation

To run maxmatch.py, a file name and string must be given as arguments. The file name is the name of the dictionary file. In this case, it is "tokenDictionary.txt". The second argument is the sentence that will be tokenized using the maxmatch implementation.
 
`python maxmatch.py tokenDictionary.txt 'some sentence'`
