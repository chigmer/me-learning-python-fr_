def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    
    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width)


# Test cases
try:
    box_print('*', 4, 4)
    print()  # empty line for separation
    
    box_print('O', 20, 5)
    print()
    
    box_print('x', 1, 3)          # this will raise exception
    print()
    
    box_print('ZZ', 3, 3)         # this will raise exception
except Exception as err:
    print('An exception happened: ' + str(err))


# Another separate test
print("\nSecond test:")
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))
 
  