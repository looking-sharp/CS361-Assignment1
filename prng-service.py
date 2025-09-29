import time
import random
import sys

filename = "prng-service.txt"

def writeRandomNumber():
    with open(filename, 'w') as f:
        num = random.randint(0, sys.maxsize)
        f.write(str(num))

while True:
    with open(filename, 'r') as f:
        f.seek(0)
        if(f.read().strip() == 'run'):
            time.sleep(1)
            writeRandomNumber()
    time.sleep(0.5)
