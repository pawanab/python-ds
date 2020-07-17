from abc import ABC, abstractclassmethod


class SlowDownBehavior(ABC):

  @abstractclassmethod
  def slowDown(self):
    pass


class VehicleSlowDown(SlowDownBehavior):
  def slowDown(self):
    # We apply encapsulation since as a car User
    # we only need to worry about using the brakes,
    # and not how they work
    self.__applyBrakes()

  def __applyBrakes(self):
    print("applying car brakes")


class AirplaneSlowDown(SlowDownBehavior):
  def slowDown(self):
    self.__reverseThrusters()

  def __reverseThrusters(self):
    print("reversing thrusters")


class Vehicle:
  def __init__(self, num_wheels: int, slowDownBehavior: SlowDownBehavior):
    self.num_wheels = num_wheels
    self.slowDownBehavior: SlowDownBehavior = slowDownBehavior

  def slowDown(self):
    self.slowDownBehavior.slowDown()



class Car(Vehicle):
  def __init__(self, wheels: int, slowDownBehavior: SlowDownBehavior):
    # Here we call the parent's constructor
    super().__init__(wheels, slowDownBehavior)
  
  # Car-specific methods follow
  def stopAtTrafficLights():
    pass


class Airplane(Vehicle):
  def __init__(self, wheels: int, slowDownBehavior: SlowDownBehavior):
    # Here we call the parent's constructor
    super().__init__(wheels, slowDownBehavior)
  
  # Airplane-specific methods follow
  def stopAtTrafficLights():
    pass

 
car: Vehicle = Vehicle(4, VehicleSlowDown())
airplane: Vehicle = Vehicle(6, AirplaneSlowDown())

car.slowDown()
airplane.slowDown()