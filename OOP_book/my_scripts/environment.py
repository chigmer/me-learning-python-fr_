import random,time
import os

class Entity():
    def __init__(self,name,range_,MAX_row,MAX_column):
        self.row = MAX_row
        self.column = MAX_column
        self.range_ = range_
        self.x = random.randint(0, MAX_row - 1)
        self.y = random.randint(0, MAX_column - 1)
        #(row,column) (x,y)
        self.icon = name[0].upper()
        self.name = name
        #print(f"initial POS: {self.x},{self.y}")
    def move(self):
        dx = random.randint(-self.range_, self.range_)
        dy = random.randint(-self.range_, self.range_)

        self.x = (self.x + dx) % self.row
        self.y = (self.y + dy) % self.column

        #print(f"POS: {self.x},{self.y}")
class World():
    def __init__(self,max_row,max_column,*entities):
        self.max_row = max_row
        self.max_column = max_column
        self.entities = entities
    def render(self):
        grid = [[" - " for _ in range(self.max_row)] for _ in range(self.max_column)]
        for entity in self.entities:
            x_pos = entity.x
            y_pos = entity.y
            grid[y_pos][x_pos] = f" {entity.icon} "
            #nested lists are so confusing.
         
        for row in grid:
            print("".join(row))
    def print_entities(self):
        unique_entities = []
        for entity in self.entities:
            unique_entities.append((entity.icon,entity.name))
        unique_entities= list(set(unique_entities))
        for i in unique_entities:
            print(f"{i[0]}: {i[1]}\n")
        
        
        
        
                

def main():
    Tree1 = Entity("Tree",0,16,10)
    Tree2 = Entity("Tree",0,16,10)
    Tree3 = Entity("Tree",0,16,10)
    Dog = Entity("Dog",2,16,10)
    Cat = Entity("Cat",3,16,10) 
    bug1 = Entity("Bug",1,16,10)
    bug2 = Entity("Bug",1,16,10)
               
    Field = World(16,10,Tree1,Tree2,Tree3,Dog,Cat,bug1,bug2)
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        Dog.move()
        Cat.move()
        bug1.move()
        bug2.move()
        Field.render()
        Field.print_entities()
        time.sleep(1.2)
#10x15 area!!
if __name__ == "__main__":
    main()