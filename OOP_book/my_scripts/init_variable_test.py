#variable during instantiation

class Greet():
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hi {self.name}")
oGreet = Greet("Bob")
oGreet.greet()