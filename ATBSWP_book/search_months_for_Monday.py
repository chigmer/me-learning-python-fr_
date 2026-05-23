"Start from today (which is 2026). Move forward month by month for 10 years. Print every month and the year its in where the first day is a Monday"
from datetime import datetime
def main():    
    valid = []
    for year in range(2026,2037):
        for month in range(1,13):            
            full = datetime(year,month,1)
            if full.isoweekday() == 1:
                valid.append(full)
    print("Months that have the first day being a monday\nin the span of 10 years: ")    
    for i,date in enumerate(valid):
        print(f"{i+1}. {date.strftime('%B, %Y')} ")
       
if __name__ == "__main__":
    main()