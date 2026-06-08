class Dog():
    """
    class Dog: represents a dog using name, breed and age
    
    Usage:
        
        oDog = Dog(name,breed,age)
        
        oDog.show()
        
        oDog.edit(name=None, breed=None, age=None)"""
    def __init__(self,name,breed,age):
        if not isinstance(name,str):
            raise ValueError("Invalid type for name")
        if not isinstance(breed,str):
            raise ValueError("Invalid type for breed")
        if not isinstance(age,(float | int)):
            raise ValueError("Invalid type for age")
        self.name = name
        self.breed = breed
        self.age = age
    def show(self):
        print("Showing Dog info:")
        print(f"\nName: {self.name}\nBreed: {self.breed}\nAge: {self.age} {'year old' if self.age == 1 else 'years old'}")
    def edit(self,name=None,breed=None,age=None):
        
        if not isinstance(name, str | None):
            raise ValueError("Invalid type for name")
        if not isinstance(breed,(str | None)):
            raise ValueError("Invalid type for breed")
        if not isinstance(age,(float | int | None)):
            raise ValueError("Invalid type for age")
        if name:
            
            self.name = name
        if breed:
            
            self.breed  = breed
        if age:
            
            self.age = age
        
    
dog = Dog("Pookie","Chihauhau",1.5)


dog.show()
print("\n--Changed dog info!!--\n")
dog.edit("New dawg","SomeBreed",2)

dog.show()
