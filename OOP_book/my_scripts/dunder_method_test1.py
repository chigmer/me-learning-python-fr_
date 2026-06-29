#dunder or magic methods?
class Bag():
    def __init__(self,*args):
        self.inventory = args
    def __len__(self):
        return len(self.inventory)
    def __repr__(self):
        inventory = [repr(i) for i in self.inventory]
        return f"Bag({', '.join(inventory)})"           
    def __iter__(self):
        return iter(self.inventory)
            
if __name__ == "__main__":
    MyBag = Bag("banana","apple","orange","catalytic converter")    
    print(len(MyBag)) #should be 4  
    print(MyBag) #repr
    for i,v in enumerate(MyBag,start=1):
        print(f"{i}. {v}")
    