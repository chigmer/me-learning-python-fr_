def say_howdy(name: str) -> None:
    print(f"Howdy, {name.title()}.")
def say_hello(name: str) -> None:
    print(f"Hello, {name.title()}.")
def greet(greeter, name):
    greeter(name)
    
    
    
if __name__ == "__main__":
    name_1,name_2 = "joe", "alice"
    
    greet(say_hello,name_1)
    greet(say_howdy,name_2)
    