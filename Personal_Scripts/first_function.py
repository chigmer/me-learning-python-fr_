
def binary_board(number):
    if number <= 1:
        return
    a = "1"
    rows = number
    while len(a) < number and number != 0:
        a += "0"
        if len(a) == number:
            break
        a += "1"
    second_line = a[1:]
    if second_line[-1] == "0":
        second_line += "1"
    else:
        second_line += "0"
        
    while True:
        print(a)
        rows -= 1
        if rows == 0:
            break
        print(second_line)
        rows -= 1
        if rows == 0:
            break
    print()  
       
if __name__ == "__main__":
    binary_board(10)
    binary_board(-10102)
    binary_board(8)
    binary_board(15)
    
    