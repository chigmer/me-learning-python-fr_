def chess_pos() -> dict:
        
    positions = ""
    for character in "abcdefgh":
        for num in range(1,9):
            positions += f"{character}{num} "
            
            
    
            
    return positions.split()
    
if __name__ == "__main__":
    print(chess_pos())
    
    
        
        
        
