class Reverse:
    '''
    Iterators are objects that can be iterated upon.
        Python uses the __iter__() method to return an iterator object of the class.
        The iterator object then uses the __next__() method to get the next item.
        for loops stops when StopIteration Exception is raised.
    '''
    def __init__(self, data):
        self.data = data
        self.index = len(data)


    def __iter__(self):
        return self

    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


if __name__ == "__main__":
    rev = Reverse('Pawan Arora')
    for char in rev:
        print(char,end='')

