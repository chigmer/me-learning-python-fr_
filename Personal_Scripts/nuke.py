def nuclear_bomb():
    a = []
    """
    Memory allocation stress test.
    
    This will crash Python by filling RAM.
    OS will kill the process when memory is exhausted.
    
    Educational experiment - advisable to NOT run on shared systems
    """
    while True:
        a.append([0] * 100000000)  
        #a lotta zeroes
        
        
#nuclear_bomb() #commented out for safety (you're welcome)
                        