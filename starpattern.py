def pypattern(n):
    myList = []
    for i in range(0,n):
        myList.append('* '*i)
    print("\n".join(myList))


def numberPattern(n):
    for i in range(0, n+1):
        for j in range(0, i):
            print(j+1, end='\t')
        print('\n')
        


def contnum(n):
    '''
    n being the rows
    '''
    varToPrint = 65
    for i in range(0, n):
        for j in range(0, i+1):
            print(chr(varToPrint), end=' ')
            varToPrint+=1
        print('\r')


if __name__ == "__main__":
    # pypattern(5)
    # numberPattern(5)
    contnum(5)