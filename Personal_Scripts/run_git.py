import sys
import subprocess as sp
def check_err(process:sp.CompletedProcess):
    if process.returncode != 0:
        print(process.stderr)
        sys.exit(1)
    else:
        return #for explicitness
def yes_or_no(input_message:str) -> bool:
    while True:
        user = input(f"{input_message} (y/n)\n\n>").lower().strip()
        if user == "y":
            return True
        elif user == "n":
            return False
        else:
            print("Invalid")
           
def main():
    status = sp.run(
    ["git", "status", "--untracked-files=all"],
    capture_output=True,
    text=True
)
    check_err(status)  
    print(status.stdout)
    
    
    choice = yes_or_no("Add Files?")
    if not choice:
        sys.exit(0)
    add = sp.run(["git","add","."],capture_output=True,text=True)
    check_err(add)
    while True:
        try:
            user = input("Commit Message>").strip()
            if not user:
                print("commit message must not be empty")
                continue
            elif len(user) <= 3:
                print("I wouldnt do that if I were you. ")
                continue
            #etiquette
            else:
                break
        except KeyboardInterrupt:
            sys.exit(0)
            #adding this because it genuinely committed it without me knowing before
            
    commit = sp.run(
    ["git","commit","-m",user],
    capture_output=True,
    text=True)
    check_err(commit)
    print(f"commit:\n\n{commit.stdout}")
    choice = yes_or_no("Push Changes?")
    if choice:
        push = sp.run(["git","push"],capture_output=True,text=True)
        check_err(push)
        print(push.stdout)
    else:
        reset = sp.run(["git","reset", "--mixed", "HEAD~1"],capture_output=True,text=True)
        check_err(reset)
        
    
        
    
    
if __name__ == "__main__":
    main()