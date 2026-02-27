def green_text(text):
       if not isinstance(text,str):
           print("type a string.")
           return 
       return f"\033[32m{text}"   # green text in terminal
   
   
if __name__ == "__main__":
       print(green_text("boom ") * 10)
       