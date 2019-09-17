import sys, re
#this is the standard tokeniser for english
abbr = ['etc.', 'e.g.', 'i.e.']

def tokenise(line, abbr):
    line = re.sub(r'([\(\)"?:!;])', r' \g<1> ', line)
    #the following 2 lines check if it is a number with commas, only add spaces before
    #and after the numbers
    line = re.sub(r'([^0-9])', r'\g<1> ', line)
    line = re.sub(r'([^0-9])', r' \g<1>', line)
    #this replaces double spaces with single spaces (when 2 or of the above symbols appear next
    #to each other)
    line = re.sub(r'  +', ' ', line[:-1])

    output = []
    for token in line.split(' '):
        if token.strip() != '' and token[-1] == '.' and token not in abbr:
            token = token[:-1] + ' .'
        output.append(token)

    return ' '.join(output)

line = sys.stdin.readline()

while line != '':
    print(tokenise(line.strip('\n'), abbr))
    line = sys.stdin.readline()

#cat ../00_Unix/wiki.txt | python3 segmenter.py | python3 tokeniser.py

#problems with this is that sometimes you want : to be included in the token ex: 1:00pm
#to check the numerical number of spaces you can use:
#echo "this is a test." | hexdump -xc
#a space has 20 as its number, anything else that looks like a space but is not 20 is different

