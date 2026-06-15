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
    def __init__(self,max_row,max_column,entities=None,empty_cell= "-"):
        self.entities = entities if entities is not None else []
        self.max_row = max_row
        self.max_column = max_column
        self.empty_cell = empty_cell.center(len(empty_cell) + 2)  
        self.entities = entities
    def render(self):
        grid = [[self.empty_cell for _ in range(self.max_row)] for _ in range(self.max_column)]        
        for entity in self.entities:
            x_pos = entity.x
            y_pos = entity.y
            collision = f"{(grid[y_pos][x_pos]).strip()}{entity.icon}"
            grid[y_pos][x_pos] = f" {entity.icon} " if grid[y_pos][x_pos] == self.empty_cell else collision.center(len(collision) + 2)
            #nested lists are so confusing.
        
        for row in grid:
            print("".join(row))
    def print_entities(self):
        unique_entities = []
        for entity in self.entities:
            unique_entities.append((entity.icon,entity.name,entity.range_))
        unique_entities= list(set(unique_entities))
        for i in unique_entities:
            print(f"{i[0]}: {i[1]}\nSpeed: {i[2]}")
    def move_entities(self):
        for entity in self.entities:
            entity.move()
        
        
        
        
                

def main():
    
    LENGTH = 10
    WIDTH = 16
    entity_names = ["Tree"] * 4 + ["Dog","Cat","Bush"]
    entity = []
    for name in entity_names:
        if name == "Tree" or name == "Bush":
            speed = 0
        else:
            speed = random.randint(1,3)
            
        entity.append(Entity(name,speed,WIDTH,LENGTH))                     
    Field = World(WIDTH,LENGTH,entity,empty_cell = "•")
    while True:
        os.system("cls" if os.name == "nt" else "clear")        
        Field.render()
        Field.move_entities()
        Field.print_entities()
        time.sleep(1.2)
#10x15 area!!
if __name__ == "__main__":
    main()