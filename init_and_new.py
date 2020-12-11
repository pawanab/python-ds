class TestIntNew(object):
    
    def __init__(self, name):
        self.name = name
        print('init called')

    def __new__(cls, *args, **kwargs):
        print('New called')
        return super(TestIntNew, cls).__new__(cls)
        
    def __repr__(self):
        return f'TestInitandNEW__{self.name}'

    def __str__(self):
        return f'{self.name}'

    def __call__(self, *args, **kwrags):
        print('Call called.')
        sum = 0
        for a in args:
            sum += a
        return sum



if __name__ == '__main__':
    print(type(TestIntNew))
    a = TestIntNew('Pawan')
    print(a(1,2,3))
    # print(a.name)
    """ print(type(a))
    print(repr(a))
    print(str(a))

    print(ord('A'))  """