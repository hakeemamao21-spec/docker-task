import random

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
        

class Vizsla(Animal):
    Tag = 1  
    
    def __init__(self, age):
        Animal.__init__(self, age)
        self.furColor =None
        self.longEar =None
        
        
    def set_furColor(self, color):
        self.furColor = color
        
    def set_longEar(self, longEar):
        self.longEar = longEar
        
    def get_furColor(self):
        return self.furColor
        
    def get_longEar(self):
        return self.longEar
        
    def age_difference(self, other):
        return abs(self.age - other.age)
        
    def __str__(self):
        return "Vizsla: " + str(self.name) + " : " + str(self.age) + \
               " Years old, rid = " + str(self.Tag) + \
               ", Color " + str(self.furColor) + \
               ", Long Ear: " + str(self.longEar)


print("\n---- Vizsla tests ----")
Gabor = Vizsla(3)
Baiv = Vizsla(16)

Gabor.set_name("Gabor")
Gabor.set_furColor("light red")
Gabor.set_longEar(False)

Baiv.set_name("Baiv")
Baiv.set_furColor("dark red")
Baiv.set_longEar(True)

print(Gabor)
print(Baiv)
print("Age difference between Baiv and Gabor:", Baiv.age_difference(Gabor))