#Devise a way to find an element in the rotated array in O(log n) time.

def findPivot(arr:list, haystack: list, needle: any):
    print(haystack, end="\t")
    sizeOfList = len(haystack)
    print("size => ", sizeOfList, end="\t")
    if sizeOfList <= 1:
        return -1

    middleIndex = sizeOfList//2
    middleIndexEle = haystack[middleIndex]

    print(middleIndex, middleIndexEle, sep=" => ")
    
    # print(type(needle), middleIndex, type(haystack[middleIndex]), sep=' => ')
    if (needle == middleIndexEle):
        # print('===========================================')
        return middleIndex + (sizeOfList-1)
    elif needle < middleIndexEle:
        return findPivot(arr, arr[middleIndex::], needle)
    elif needle > middleIndexEle:
        return findPivot(arr, arr[0:middleIndex], needle)
        


# def searchEle(arr, meedle, index):

if __name__ == '__main__':
    l = list(map(int,input('Enter space sperated values: ').split(' ')))
    d = int(input(f'please entry number to search : '))
    
    r = findPivot(l, l, d)
    print(r)
