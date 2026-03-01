"""Fantasy Game Inventory Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory is a dictionary whose keys are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on."""

"""Dear Al Sweigart, I dont like fantasy games. please structure your book to fit a broader audience"""
def countstuff(inventory:dict) -> None:
    print("inventory: \n")
    if not all(isinstance(v, int) for v in inventory.values()):
        print("Error: Inventory counts must be integers.")
        return
        
    count = 0
    try:
        for item,value in inventory.items():
            print(value, item)
            if isinstance(value,int):
                count += value
            else:
                raise ValueError("your inventory is missing item amounts.")
        print(f"total: {count}")
    except Exception as e:
        print(f"im not going to bother what made you get this error message, figure it out yourself. \n {e}")        
        
#import intelligence
def add_to_inventory(inventory_2, added_items):            
    for item in added_items:
        inventory_2.setdefault(item,0)
        inventory_2[item] += 1
    return inventory_2
                   
         
if __name__ == "__main__":    
    inv = {'gold coin': 42, 'rope': 1}
    print(inv)  
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] 
    print(dragon_loot)
    add_to_inventory(inv, dragon_loot)
    countstuff(inv)
 