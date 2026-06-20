class Car:
    def __init__(self,brand,model,mileage):
        self.brand = brand
        self.model = model
        if mileage and isinstance(mileage,int):
            self.mileage = mileage
        else:
            self.mileage = 0
    def show(self):
        print(f"{self.brand}, {self.model}\nMileage:{self.mileage}")
        
