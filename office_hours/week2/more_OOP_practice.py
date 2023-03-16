# Demo with more classes
class Fruit:
    def __init__(self, name, shape, color, size, is_edible = True): # 
        self.name = name
        self.shape = shape
        self.color = color
        self.size = size
        self.is_edible = is_edible

    def eat(self):
        print(f"This fruit called {self.name} has now been eaten!")
        self.is_edible = False


orange = Fruit("Orange","spherical","orange",5, True)
print(orange.size)
apple = Fruit("Apple","roundish","red",6,True)
print(apple.size)
orange.eat()
apple.eat()