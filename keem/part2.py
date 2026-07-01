
class Animal:
    tag = 1

    def __init__(self, age):
        self.age = age
        self.aid = Animal.tag
        Animal.tag += 1

    def get_age(self):
        return self.age

    def get_aid(self):
        return self.aid

    def __add__(self, other):
        return Animal(0)


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def __add__(self, other):
        return Rabbit(0, self, other)

    def sibling(self, other):
        """
        Returns True if rabbits share AT LEAST ONE parent.
        """
        if not self.parent1 or not self.parent2:
            return False
        if not other.parent1 or not other.parent2:
            return False

        return (
            self.parent1 is other.parent1 or
            self.parent1 is other.parent2 or
            self.parent2 is other.parent1 or
            self.parent2 is other.parent2
        )

r3 = Rabbit(3)
r4 = Rabbit(4)
r5 = Rabbit(5)
r6 = Rabbit(6)

r7 = r5 + r6  
r8 = r6 + r4   
r9 = r4 + r3   

print(r7.sibling(r8))   
print(r7.sibling(r9))   
print(r8.sibling(r9))   