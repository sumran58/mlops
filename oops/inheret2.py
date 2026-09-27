#derived  inheritence  with the super keyword 

class Animal:
    def __init__(self):
        self.name='buddy'

    def sound(self):
        print(f"{self.name} makes the sound")

class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed=breed

    def speak(self):
        super().speak() #clls the parent class method 
        print(f"{self.name} it is type of breed called {self.breed}")

d=Dog("golden retriver")
d.sound()