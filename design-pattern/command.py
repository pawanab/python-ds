import os


class RenameCommand(object):
    def __repr__(self):
        return f'<RenameCommand {self.__from} => {self.__to} >'

    def __str__(self):
        return f'Rename {self.__from} TO {self.__to}'

    def __init__(self, from_name, to_name):
        self.__from = from_name
        self.__to = to_name

    def execute(self):
        os.rename(self.__from, self.__to)

    def undo(self):
        os.rename(self.__to, self.__from)


class History(object):

    def __init__(self):
        self.__history = list()

    def execute(self, command):
        self.__history.append(command)
        command.execute()
    
    def undo(self):
        self.__history.pop().undo()
    
    def show(self):
         [print(history) for history in self.__history]




if __name__ == "__main__":
    history = History()
    history.execute(RenameCommand('./closure_logs.log', './closure_logs.log1'))
    history.execute(RenameCommand('./closure_logs.log1', './closure_logs.log'))
    history.show()
    history.undo()
    history.undo()
    history.show()
