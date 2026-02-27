"""cat name saver 101"""

cat_names = [] 

while True:
    
    cat = input(f"enter the name of cat {len(cat_names) + 1} (enter nothing to stop): ")
    
    if cat == '':
        break        
    cat_names.append(cat)
print("Your cats: ")
if len(cat_names) == 0:
    print("Youre.. catless")
    
for feline in cat_names :
    print(feline)
   
    
    
    