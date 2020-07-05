# This is special class. Is is being used a lot in different projects throughout the empire.
# It is extremely important to NOT change the way other tools interact with this class.
# However we have a hunch it could be improved. Do you have any ideas?

class Units:
    
    def __init__(self):
        self._unit1 = 0
        self._unit2 = 0
        self._unit3 = 0
        self._unit4 = 0
        self._unit5 = 0

    @property
    def unit1(self):
        return self._unit1

    @unit1.setter
    def unit1(self, unit):
        self._unit1 = unit if unit % 2 == 0 else 0

    @property
    def unit2(self):
        return self._unit2

    @unit2.setter
    def unit2(self, unit):
        self._unit2 = unit if unit % 2 == 0 else 0

    @property
    def unit3(self):
        return self._unit3

    @unit3.setter
    def unit3(self, unit):
        self._unit3 = unit if unit % 2 == 0 else 0

    @property
    def unit4(self):
        return self._unit4

    @unit4.setter
    def unit4(self, unit):
        self._unit4 = unit if unit % 2 == 0 else 0

    @property
    def unit5(self):
        return self._unit5

    @unit5.setter
    def unit5(self, unit):
        self._unit5 = unit if unit % 2 == 0 else 0 


#Improved Version

class UnitProb:
    """A utility class that does brain surgery 
    on the Units class by taking ownership of 
    the __get__ and __set__ methods of it's 
    instances"""

    def __init__(self, name):
        self.name = "_" + name

    def __get__(self, instance, cls):
        return getattr(instance, self.name)

    def __set__(self, instance, unit):
        if not isinstance(unit, int):
            raise TypeError("Integer Expected")
        value = unit if unit % 2 == 0 else 0
        setattr(instance, self.name, value)


class Units:
    unit1 = UnitProb("unit1")
    unit2 = UnitProb("unit2")
    unit3 = UnitProb("unit3")
    unit4 = UnitProb("unit4")
    unit5 = UnitProb("unit5")

    def __init__(self):
        self._unit1 = 0
        self._unit2 = 0
        self._unit3 = 0
        self._unit4 = 0
        self._unit5 = 0
