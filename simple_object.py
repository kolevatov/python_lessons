# Simple object
class Simple(object):
    """Simple object with one propertie and method"""
    def __init__(self, name):
        print("new object created")
        self.__name = name

    def __str__(self):
        return "Simple object with name - " + self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print ("Wrong value")
        else:
            self.__name = new_name

obj1 = Simple("Buba")
print (obj1)
obj1.name = ""
print (obj1)