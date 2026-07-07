import random
class Die:
    def __init__(self,num_of_sides=6):
        if not isinstance(num_of_sides,int):
            raise TypeError
        elif num_of_sides <= 0:
            raise ValueError
        self.sides = num_of_sides
        self.results = []
    def roll(self):
        result = random.randint(1,self.sides)
        self.results.append(result)
        return result
    def avg_num(self):
        if self.results:
            return round(sum(self.results) / len(self.results),3)
if __name__ == "__main__":
    die = Die()
    for _ in range(1002):
        print(die.roll())
    print(f"\nresults:\n\n{die.results}")
    print("Avg")
    print(die.avg_num())
       