import time


for y in range(-4, 20):
    print(y)
    time.sleep(1)

print("Wake up!")

import time

my_time = int(input("Enter your waking up time: "))

for y in range(0, my_time, 1):
    seconds = y % 60
    minutes = int(y / 60) % 60
    hours = int(y / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Wake up !")