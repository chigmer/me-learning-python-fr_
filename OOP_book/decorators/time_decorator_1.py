#test, no fancy syntax yet.
from datetime import datetime
def time_decorator(func):
    def time_wrapper():
        hour = datetime.now().hour
        if hour <= 6 or hour >= 22:
            print("extra behavior:\nits too late to run this script!")           
            return
        else:
            func()
    return time_wrapper
def print_something() -> None:
    print(f"its currently {datetime.now().strftime('%I:%M %p')}. Your neighbors are probably awake right now")
    
if __name__ == "__main__":
     print_something_decorated = time_decorator(print_something)
     print_something_decorated()
    