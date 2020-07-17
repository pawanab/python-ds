def func():
    # Do anything here
    pass

# User-defined functions have a __dict__ property:
print("__dict__ of func:", func.__dict__)
func.temp = 1
print("__dict__ of func after assignment:", func.__dict__)

class A:
  def __init__(self, prop):
    self.prop = prop

  def funcA(self):
    print("Asgasga")

# Class definitions have a __dict__ property:
print("__dict__ of A:", A.__dict__)

# Class instantiations have a __dict__ property:
a = A(123)
print("__dict__ of a:", a.__dict__)

print("-------------------------------------- \n")


class MonostateSingleton:
  __shared_state = {'apikey': 'xxxxxxxxxxxxxxxxxxx'}

  def __init__(self):
    # Because dictionary assignments are by reference, we force 
    # self.EOFError__dict__ to be common to all future instantiations
    self.__dict__ = self.__shared_state
    self.x = 1


obj = MonostateSingleton()

obj1 = MonostateSingleton()

# Notice that the two objects reside at different addresses, thus 
# they are different objects:
print("property x: {} of obj at: {}".format(obj.x, obj))
print("property x: {} of obj1 at: {}".format(obj1.x, obj1))

# Notice that the 'x' property is part of the __dict__
print(obj.__dict__, obj1.__dict__)

# We change the x propert only of obj 
obj.x = "LALALA"

# However, because the two objects share the same __dict__ and this is 
# where class attributes are stored, the change is also visible in obj1
# We have thus achieved a SHARED STATE:
print("property x: {} of obj at: {}".format(obj.x, obj))
print("property x: {} of obj1 at: {}".format(obj1.x, obj1))

print(obj.__dict__, obj1.__dict__)