# autovivification => the automtic creation of array and hash every time undefined value is dereferenced.

class Tree(dict):

    def __missing__(self, key):
        value = self[key] = type(self)()
        return value



if __name__ == "__main__":
    tree = Tree()
    tree['carnivora']['canis']['c.lupus'] = 'c.l.familiaris'
    tree['carnivora']['felis'] = 'f.catus'
    
    print(tree)