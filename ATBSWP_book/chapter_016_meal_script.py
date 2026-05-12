import sqlite3
import re
import sys
try:
    print("setting up inflect\n(patience is a virtue)")
    import inflect

except ModuleNotFoundError:
    print("this script uses the third party module \"inflect\"\ninstall it by running\n\npip install inflect")    
    sys.exit(1)
conn = sqlite3.connect("meal_and_ingredients.db")
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS meals (meal_id INTEGER PRIMARY KEY, name TEXT UNIQUE) STRICT""")

cur.execute("CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY, name TEXT UNIQUE) STRICT")

cur.execute("CREATE TABLE IF NOT EXISTS middle (meal_id INTEGER,ingredient_id INTEGER, PRIMARY KEY (meal_id,ingredient_id),FOREIGN KEY (meal_id) REFERENCES meals(meal_id),FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)) STRICT")




"""Then, write a program that prompts the user for input. If the user enters 'quit', the program should exit. The user can also enter a new meal
name, followed by a colon and a comma-delimited list of ingredients: 'meal:ingredient1,ingredient2'. Save the meal and its ingredients in the meals and ingredients tables. Finally, the user can enter the name of a meal or ingredient. If the name
appears in the meals table, the program should list the meal’s ingredients. If the name appears in the ingredients table, the program should list every meal that uses this ingredient. For example, the output of the program could look like this:"""

p = inflect.engine()
def normalize_ingredient(name):
    
    name = str(name).strip().lower()
    singular = p.singular_noun(name)

    singular = p.singular_noun(name)

    if singular:
        return singular

    return name
def valid_recipe_format(user_input):
    

    pattern = re.compile(r"""
    ^\s* #valid if it starts with a whitespace or not
    
    ([^:,]+) #dish name, one or more characters which are not a colon or comma
    
    \s*:\s* #mandatory colon, whitespace is valid on both sides
    
    ([^:,]+) #mandatory ingredient, must not have a colon or comma inside of it
    
    (\s*,\s*[^:,]+)* #ingredients, optional
    
    \s*$ #optional whitespace
""", re.VERBOSE)
    return bool(re.fullmatch(pattern,user_input))

    
def extract_info(user_input):
    user = user_input.strip().split(":",1)
    recipe = {}
    dish = user[0].lower()
    ingredients = user[1].split(',')
    recipe[dish] = [i.lower().strip() for i in ingredients]
    return recipe
#print(extract_info("onigiri:rice, nori, salt, sesame seeds"))

def main():
    print("Welcome. Type --help for help\nType exit to exit")
    while True:
        user = input("[VIEW]>").strip().lower()
        if user == "--help":
            print("COMMANDS:\n-view\n-insert\n-exit\n\nThis program will show the ingredients of a meal you type, or what meals use an ingredient that you've typed.\n\nAlternatively, you can also insert a dish yourself, simply type 'insert' to switch to 'writing mode'\n(NOTE: you must manually type 'view' if you want to back to viewing mode)\n\nTo insert a dish, follow the command below.\n\nUsage:\n<dish_name>: <ingredient_1>,<ingredient_2>,...\n\nExample Usage 1:\n>insert\n>fried eggs: egg\n\nExample Usage 2:\n>insert\n>onigiri:rice, nori, salt, sesame seeds\n\nView Mode:\ntype in any ingredient or dish, and itll automatically look up the database for you and display the appropriate information")   
            print("\n\nExiting the Food Lookup Fiasco:\nsimply type in 'exit'.\n\nExample Usage:\n\n>exit (it will exit shortly)")    
        elif user == "insert":
            while True:
                user_dish = input("[INSERT]>")
                if valid_recipe_format(user_dish):                    
                    data = extract_info(user_dish)
                    #my tables:
                    #meals: meal_id, name
                    #ingredients: ingredient_id, name
                    meal = tuple(data.keys())
                    ingredients = [normalize_ingredient(i) for i in data[meal[0]]]               
                    #print(ingredients)
                    print("inserting dish + ingredients to database..")                  
                    
                    cur.execute("INSERT OR IGNORE INTO meals (name) VALUES (?) RETURNING meal_id",meal)
                    meal_id = cur.fetchone()[0]
                    if meal_id:
                        print(f"INSERTED DISH: {meal[0]}")        
                    else:
                        cur.execute("SELECT meal_id FROM meals WHERE name = ?", meal)
                        meal_id = cur.fetchone()[0]
                        print(f"{meal[0]} already exists")            
                    for i in ingredients:
                        cur.execute("INSERT OR IGNORE INTO ingredients (name) VALUES (?) RETURNING ingredient_id",(i,))
                        ing_id = cur.fetchone()
                        if ing_id:
                            ing_id = ing_id[0]
                            print(f"INSERTED INGREDIENT: {i}")
                        else:
                            
                            cur.execute("SELECT ingredient_id FROM ingredients WHERE name = ?", (i,))
                            ing_id = cur.fetchone()[0]
                            print(f"{i} already exists")
                        cur.execute("INSERT OR IGNORE INTO middle (meal_id, ingredient_id) VALUES (?, ?)", 
                                    (meal_id, ing_id))
                        
                    #print(f"MEAL ID: {meal_id}\nINGREDIENT_IDS: {ing_id}")
                    conn.commit()
                elif user_dish == "view":
                    break
                else:
                    print("Invalid insertion.")
                    print("Expected:\n<dish>:<dish_name>,...")
        elif user == "exit":
            print("exiting..")
            break
        else:
            #view logic
            
            cur.execute("SELECT name FROM meals WHERE name = ?", (user,))
            meal = cur.fetchone() #does it exist? check
            if meal:
                meal = meal[0]
                #CREATE TABLE IF NOT EXISTS middle (meal_id INTEGER,ingredient_id INTEGER, PRIMARY KEY (meal_id,ingredient_id),FOREIGN KEY (meal_id) REFERENCES meals(meal_id),FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id))
                #triple join, select ingredients 
                cur.execute("SELECT i.name FROM ingredients i JOIN middle m on i.ingredient_id = m.ingredient_id JOIN meals ml on ml.meal_id = m.meal_id WHERE ml.name = ?",(meal,))
                # joins the exact rows where both ingredient_id and meal_id are in the same row (meaning related)
                print(f"ingredients for: {meal}\n")
                for i in cur:
                    print(i[0])
                print()
            elif meal is None:  
                cur.execute("SELECT name FROM ingredients WHERE name = ?", (user,))
                ingredient = cur.fetchone()
                if ingredient:       
                    ingredient = ingredient[0]
                    cur.execute("SELECT ml.name FROM meals ml JOIN middle m ON ml.meal_id = m.meal_id JOIN ingredients i ON i.ingredient_id = m.ingredient_id WHERE i.name = ?", (ingredient,))
                    print(f"Meals that use {ingredient}:\n")
                    for i in cur:
                        print(i[0])
                    print()                
                else:
                    print(f"Couldnt find any dishes or ingredients that match: {user}")
       

                
            
        
            
            
if __name__ == "__main__":
    main()
    #Ive built a junction table. how cool is that
    #proof i made it, a junction table stores unique pairs of two integers from the primary keys of two tables, that combination acts
    #as its own primary key, the triple join is the fun part
    
    #if (per validation) a value (with its unique id) exists on a table, the first join will join the junction tables rows which matches the id of the value we gave
    #The WHERE clause only preserves the rows which have the ml.name (meal name) of the original value
    #the second join defines the second part of the pair, it stitches rows from the other table to define what the integers name actually is (junction tables id to the tables own id)
                   
