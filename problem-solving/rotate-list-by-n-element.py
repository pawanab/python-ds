import sys

def rotateListByNumber_using_temp(dataList: list, sizeofList :int, rotationIndex: int):
    _slicedList = dataList[:rotationIndex]
    
    return dataList[rotationIndex::] + _slicedList



if __name__ == '__main__':
    l = input('please entry number by comma seprated: ').split(' ')
    n = len(l)
    d = int(input(f'please entry number rorate should be less than {n} : '))
    print(d%n)
    
    if d > n:
        print('wrong input please try again.')
        sys.exit()
    

    result = rotateListByNumber_using_temp(l, n, d)
    print(result)


    