time_1 = 1,50
time_2 = 2,45
def format_duration(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60

    parts = []

    if hours:
        parts.append(f"{hours} hour" + ("s" if hours != 1 else ""))

    if minutes:
        parts.append(f"{minutes} minute" + ("s" if minutes != 1 else ""))

    if not parts:
        return "0 minutes"

    return " and ".join(parts)
def calculate(a:tuple,b:tuple):
    total = (a[0] * 60) + (b[0] * 60) + a[1] + b[1]
    return total
if __name__ == "__main__":
    print("Input first value:\n<HOUR:MINUTE>")
    val = []
    for i in range(1,3):
        print(f"value {i}:")
        while True:
            user = input("hr>").strip()
            try:
                user = int(user)
            except ValueError:            
                print("Invalid")
                continue
            if user < 0:
                print("Invalid")
                continue
            else:
                break
        val.append(user)
        while True:
            user = input("min>").strip()
            try:
                user = int(user)
            except ValueError:
                print("Invalid")
                continue
            if user >= 60:
                print("Invalid")
                continue
            elif user < 0:
                print("Invalid")
                continue
            else:
                break
        val.append(user)
    total = calculate(val[:2],val[2:])
    print("\n\n\n")
    print(format_duration(total))