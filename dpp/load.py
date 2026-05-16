import random

tasks = [random.randint(1, 10) for _ in range(10)]
nodes = [0, 0, 0]

# 🔹 Static Load Balancing (Round Robin)
for i, t in enumerate(tasks):
    nodes[i % len(nodes)] += t

print("Static Load:", nodes)

# 🔹 Dynamic Load Balancing (Assign to least loaded node)
nodes = [0, 0, 0]

for t in tasks:
    idx = nodes.index(min(nodes))
    nodes[idx] += t

print("Dynamic Load:", nodes)
