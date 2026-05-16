import random

file = "log.txt"

# Read last checkpoint
try:
    f = open(file, "r")
    last = int(f.read())
    f.close()
except:
    last = 0

print("Starting from step:", last)

try:
    for i in range(last + 1, 11):
        print("Step:", i)

        # Save checkpoint
        f = open(file, "w")
        f.write(str(i))
        f.close()

        # Simulate failure
        if random.random() < 0.3:
            raise Exception("Crash")

except:
    print("Failure! Restart program to recover.")
