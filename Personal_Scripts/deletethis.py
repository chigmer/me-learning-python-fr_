def printTable(table:list) -> None:
    for i in table:
        print(i)
        for item in i:
            print(i[item])
            print(item)
            

if __name__ == "__main_":
    tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
    print("shit")
    print("i should be seeing this but im not\n how am i supposed to continue")
    #update. im such a dumb piece of ####. the if statement is incomplete. 
    #better save this as an artifact of the past.
    