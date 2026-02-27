print("Type literally anything dude.")
item = input(">")
item = item.lower().strip()
item += " "
a = item * 10


for i in a:
    print(i,end="")
    