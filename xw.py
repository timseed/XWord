import sys

def check_word(word,clue):
    '''

    :param word: The Dictionary offering
    :param clue: Our guess with spaces in between letters
    :return: True False
    '''

    if len(word) == len(clue):
       for x in range(len(word)):
           if word[x]==clue[x] or clue[x]==' ':
              junk=1
           else:
              return False
       return True
    else:
        return False

if len(sys.argv)==2:
    print(str.format('Checking <{}>',sys.argv[1]))
    with open('words.txt','r') as ifp:
        for line in ifp:
            line=line.rstrip().lstrip().lower()

            if check_word(line,sys.argv[1].lower()):
                print(str.format('{}',line))
else:
    print("Incorrect errors")