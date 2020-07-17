class Window:
    __toolkit = ""
    __purpose = ""

    def __init__(self, toolkit, purpose):
        self.__toolkit = toolkit
        self.__purpose = purpose

    def getType(self):
        return self.__purpose

    def getTookkit(self):
        return self.__toolkit


class GtkToolboxWindow(Window):

    def __init__(self):
        Window.__init__(self, 'gtk', 'ToolboxWindow') 


class GtkLayerWindow(Window):

    def __init__(self):
        Window.__init__(self, 'gtk', 'LayerWindow')


class GtkMainWindow(Window):

    def __init__(self):
        Window.__init__(self, 'gtk', 'MainWindow')


class QtToolboxWindow(Window):

    def __init__(self):
        Window.__init__(self, 'qt', 'ToolboxWindow') 


class QtLayerWindow(Window):

    def __init__(self):
        Window.__init__(self, 'qt', 'LayerWindow')


class QtMainWindow(Window):

    def __init__(self):
        Window.__init__(self, 'qt', 'MainWindow')


# Abstract factory class
class UIFactory:
    def getToolboxWindow(self):
        pass
    
    def getLayerWindow(self):
        pass
    
    def getMainWindow(self):
        pass

if __name__ == "__main__":
    print('Pawan Arora')
