import time
def calculate_num():
    a = 3
    b = 17779
    c = 10
    n = 1
    for _ in range(1000):
        n *= a
        n -= b
        n **= c
        
    return n
start = time.time()
num = calculate_num()
end = time.time()
print(f"Result: {num} Time Elapsed: {end - start:,} seconds")