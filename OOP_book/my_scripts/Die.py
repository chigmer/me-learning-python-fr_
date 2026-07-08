import random
class Die:
    def __init__(self,num_of_sides=6):
        if not isinstance(num_of_sides,int):
            raise TypeError
        elif num_of_sides <= 0:
            raise ValueError
        self.sides = num_of_sides
        self.results = [] 
        self.frequencies = {}
        self.avg_num = 0
        for i in range(self.sides):
            self.frequencies[i+1] = 0
              
    def roll(self):
        result = random.randint(1,self.sides)
        self.results.append(result)
        return result
    def calculate_stats(self):
        if self.results:
            self.avg_num = round(sum(self.results) / len(self.results),3)
            
            for i in self.results:
                
                self.frequencies[i] += 1
if __name__ == "__main__":
    die = Die()
    for _ in range(25):
        die.roll()    
    print("Current stats! (no updating)")
    print(f"sides: {die.sides}\nresults: {die.results}\nfrequencies: {die.frequencies}\navg: {die.avg_num}")
    print("After: ")
    die.calculate_stats()
    print(f"sides: {die.sides}\nresults: {die.results}\nfrequencies: {die.frequencies}\navg: {die.avg_num}")
    
    
    
       