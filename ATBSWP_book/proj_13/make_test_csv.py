import csv
import random
from pathlib import Path

files = []
for i in range(10):
    
    filename = f"test_csv_{i+1}.csv"
    files.append(Path(filename))
    
    
    with open(filename,"w",newline="") as f:
        writer = csv.DictWriter(f,["column_1","column_2","column_3"])    
        writer.writeheader()
        for _ in range(5):#rows
            num_1 = random.randint(1000,9999)
            num_2 = random.randint(1000,9999)
            num_3 = random.randint(1000,9999)
            writer.writerow({"column_1": num_1,"column_2": num_2, "column_3": num_3})   
    
for file in files:
    print(f"file {file}: {file.exists()}")
       
            