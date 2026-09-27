#multilevel inheritence 

# class Grandparent:
#     def __init__(self,name):
#         self.name=name
                 
#     def tell_story(self):
#         print(f"{self.name} tells us a story")

# class Parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# c=Child("Charlie")
# c.tell_story()
# c.work()
# c.play()

#------------------------------------------------------------------------#

#hierarchical inheritance 
class Grandparent:
    def __init__(self,name):
        self.name=name
                 
    def tell_story(self):
        print(f"{self.name} tells us a story")

class Parent1(Grandparent):
    def work(self):
        print(f"{self.name} is working")

class Parent2(Grandparent):
    def play(self):
        print(f"{self.name} is playing")

c=Parent1("Charlie")
c1=Parent2("dave")
c.tell_story()
c.work()
c1.tell_story()
c1.play()

