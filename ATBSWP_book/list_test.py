listing = ["hey", "yo", "wassup", "hello"]

def val(var: str,Ltype: list) -> bool:
    return var in Ltype
        
print(val("yo",listing))

print(val("greetings",listing))

print("end")
