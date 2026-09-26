#simple inheritence 

class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print(f"{self.name} makes the sound")

ani=Animal("generic animal")
ani.sound()