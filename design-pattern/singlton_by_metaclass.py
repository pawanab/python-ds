
### [5] ###
class MetaSingleton(type):
  _instances = {}
  
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      # now the type's __call__() is only executed if cls is not in cls._instances
      # This way we prevent new objects from being created if one exists 
      #when the constructor of classes deriving from MetaSingleton are created 
      cls._instances[cls] = super().__call__(*args, **kwargs)
      print(cls.__dict__)
    return cls._instances[cls]  

class Logger(metaclass=MetaSingleton):
  pass

logger1 = Logger()
logger2 = Logger()

# logger1 and logger2 refer to the same object
print(logger1, logger2)