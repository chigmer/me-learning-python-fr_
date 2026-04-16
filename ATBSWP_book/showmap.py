import argparse
import webbrowser
def parse_args() -> str:
    parser = argparse.ArgumentParser(
        description="allows you to open the web browser to the OpenStreetMap page from a specific address input"
    )  
    parser.add_argument("address",type=str,help="your address. (wrap address in quotes for no ambiguity)")    
    #its common knowledge to add quotes if your input could have spaces, so I get to be lazy today
    #also, i decided to skip pyperclip, ctrl v takes two keys man..
    args = parser.parse_args()
    address = args.address
    return address

        
def main():
    address = parse_args()
    webbrowser.open(f'https://www.openstreetmap.org/search?query={address}')
if __name__ == "__main__":
    main()
    #print(f"parsed args, you typed {address}") 
        