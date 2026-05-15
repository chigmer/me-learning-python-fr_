import csv
#write 5 integers in each row (ascending)

    

with open("output3.csv","w",newline='') as csv_:
      w = csv.writer(csv_)
      start = 1
      for i in range(20): 
                       
          data = list(range(start,start + 5))  
            
          print(f"Condition {i + 1}: start = {start} end = {start + 4} written: {data}") 
          w.writerow(data)
          start += 5
          
with open("output3.csv") as C:
    for i in csv.reader(C):
        print(i)
          
    
    
