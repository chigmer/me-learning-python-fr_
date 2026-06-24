class Restaurant:
    def __init__(self,name:str):
        self.name = name
        self.open = False
    def open_restaurant(self):
        self.open = True
    def close_restaurant(self):
        self.open = False
    def show_restaurant(self):
        print(f"{self.name}\nStatus: {'open' if self.open else 'closed'}")

class IceCreamStand(Restaurant):
    def __init__(self,name):
        self.served = 0
        super().__init__(name)
    def serve(self):
        if self.open:
            print("Served an Ice Cream!")
            self.served += 1
        else:
            print("Restaurant is closed!")
myStand = IceCreamStand("Za Ice Cream")
myStand.open_restaurant()
myStand.show_restaurant()
for _ in range(10):
    myStand.serve()
print(f"total ice cream served: {myStand.served}")
        
    