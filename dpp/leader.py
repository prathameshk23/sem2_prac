processes = {1: 1, 2: 1, 3: 0, 4: 1, 5: 1}


def bully(initiator):
    active = [p for p in processes if p > initiator and processes[p]]

    if active:
        for p in active:
            print(f"{initiator} -> Election -> {p}")
        coord = max(p for p in active if processes[p])
    else:
        coord = initiator

    print(f"Coordinatior is {coord}")
    return coord


def ring(initiator):
    pids = list(processes.keys())
    i = pids.index(initiator)
    msg = []

    while True:
        pid = pids[i]
        if processes[pid]:
            print(f"{pid} passes message")
            msg.append(pid)

        i = (i + 1) % len(pids)
        if pids[i] == initiator:
            break

    print(f"Coordinator is {max(msg)}")
    return max(msg)


while True:
    print("\n1.Bully 2.Ring 3.Exit")
    ch = int(input("Choice: "))

    if ch == 3:
        break

    for p, s in processes.items():
        print(f"Process {p} is {'Active' if s else 'Down'}")

    init = int(input("Initiator: "))

    if ch == 1:
        bully(init)
    if ch == 2:
        ring(init)
