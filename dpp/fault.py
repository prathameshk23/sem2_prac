import random

checkpoint = 0

try:
    with open("log.txt", "r") as f:
        checkpoint = int(f.read())
except FileNotFoundError:
    pass

print(f"Starting step {checkpoint}")

try:
    for i in range(checkpoint + 1, 11):
        print(f"Step {i}")

        with open("log.txt", "w") as f:
            f.write(str(i))

        if random.random() < 0.3:
            raise Exception("Crash")
except:
    print("A failiure as occured...Restart")
