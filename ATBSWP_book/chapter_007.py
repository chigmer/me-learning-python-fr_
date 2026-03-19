"""
Practice Questions

1. What does the code for an empty dictionary look like? 

2. What does a dictionary value with a key 'foo' and a value 42 look like? 

3. What is the main difference between a dictionary and a list? 

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'

8. What module and function can be used to “pretty-print” dictionary values?"""

answers = """
1. {}
2. {'foo': 42}, could be dict(foo=42)
3. a dictionary has no set order, and indexes can be of any data type. a list is an ordered arrangement of objects
4. KeyError
5. no difference, both lines check for key values
6.  'cat' in spam looks for a string in the dictionary's keys while 'cat' in spam.values() looks for a string in the dictionary's values (the right side of the colon)
7. spam.setdefault('color', 'black')
8. i dont know, did i miss something??
"""

"""In this chapter, we used the dictionary value {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'} to represent a chessboard. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on whether the board is valid. A valid board will have exactly one black king and exactly one white king. Each player can have at most 16 pieces, of which only eight can be pawns, and all pieces must be on a valid square from '1a' to '8h'. That is, a piece can’t be on square '9z'. The piece names should begin with either a 'w' or a 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chessboard. (This isn’t an exhaustive list of requirements, but it is close enough for this exercise.)"""

from chesscoordinates import chess_pos
print(chess_pos())



def isvalidchessboard(board:dict)-> bool:
    coords = chess_pos()
    pieces = board.values()
    #2 kings, 16 pieces total, 8 pawns, should begin with w or b
    #symbols: p, n, b, r, k, q 
    p,n,b,r,k,q,w,black = (0,0,0,0,0,0,0,0)
    
    for key in board.keys():
        if key not in coords:
            return False
    while True:
        try:
            for piece in pieces:
                if piece[1].lower() == "p":
                    p += 1
                elif piece[1].lower() == "n":
                    n += 1
                elif piece[1].lower() == "b":
                    b += 1                    
                elif piece[1].lower() == "r":
                    r += 1
                elif piece[1].lower() == "k":
                    k += 1
                elif piece[1].lower() == "q":
                    q += 1
                else:
                    return False
        except IndexError:
            return False 
        break
    
    
    for pc in pieces:
        if pc[0].lower() == "b":
                black += 1
        elif pc[0].lower() == "w":
                w += 1
        else:
            return False
        
        
       
        #since this is a simple script and i dont wanna make coding painful, im skipping the feature in chess where you can promote your pawns
    if p <= 16  and n <= 4 and b <= 4 and r <= 4 and k == 2 and q <= 2 and len(pieces) <= 32 and black <= 16 and w <= 16:
        return True
    else:
        return False
    
if __name__ == "__main__":
    standard_board = {
        # White Pieces
        'a1': 'wr', 'b1': 'wn', 'c1': 'wb', 'd1': 'wq', 'e1': 'wk', 'f1': 'wb', 'g1': 'wn', 'h1': 'wr',
        'a2': 'wp', 'b2': 'wp', 'c2': 'wp', 'd2': 'wp', 'e2': 'wp', 'f2': 'wp', 'g2': 'wp', 'h2': 'wp',
        # Black Pieces
        'a8': 'br', 'b8': 'bn', 'c8': 'bb', 'd8': 'bq', 'e8': 'bk', 'f8': 'bb', 'g8': 'bn', 'h8': 'br',
        'a7': 'bp', 'b7': 'bp', 'c7': 'bp', 'd7': 'bp', 'e7': 'bp', 'f7': 'bp', 'g7': 'bp', 'h7': 'bp'
    }

    print(f"Is board valid? {isvalidchessboard(standard_board)}")
#lets gooo     
            
#stay tuned for the other practice program
                
        
        
                
               
    
    
    
 
   
   
    

    
 
    


