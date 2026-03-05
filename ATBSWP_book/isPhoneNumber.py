def is_phone_number(text):
    if len(text) != 12: # Phone numbers have exactly 12 characters.
        return False
    for i in range(0, 3): #The first three characters must be numbers.2
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
    
    
    # The fourth character must be a dash. 
        for i in range(4, 7): # The next three characters must be numbers. 4 
            if not text[i].isdecimal():
                return False
            if text[7] != '-': # The eighth character must be a dash.
                return False
            for i in range(8, 12): # The next four characters must be numbers. 6
                if not text[i].isdecimal():
                    return False
        return True
if __name__ == "__main__":
    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        segment = message[i:i+12]
        if is_phone_number(segment):
            print(f'Phone number found: {segment}')
    print('Done')