import random

def generate_dates(num_dates: int):
    more_days = {1, 3, 5, 7, 8, 10, 12}
    few_days = {4, 6, 9, 11}
    
    dates = []
    for _ in range(num_dates):
        month = random.randint(1, 12)
        if month in more_days:
            day = random.randint(1, 31)
        elif month in few_days:
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
        year = random.randint(2015, 2026)
        dates.append(f"{month:02}-{day:02}-{year}")
    
    return dates

# Example usage
date_list = generate_dates(50)
print(date_list)
