def get_momentum(m,v) -> float:
    return m * v

if __name__ == "__main__":
    print("momentum script 101")
    import sys
   
    while True:
        try:
            mass = float(input("mass: "))
            velocity = float(input("velocity: "))
        except ValueError:
            print("you typed smth wrong lol")
            continue
        except KeyboardInterrupt:
            print("sure bro")
            sys.exit()
        break
    print(f"The momentum is {get_momentum(mass,velocity):,} kgm/s")
#moduleable fr 

        
    
    