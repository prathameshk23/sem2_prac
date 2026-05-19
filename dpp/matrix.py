import multiprocessing, time

n = 3

a = [[i + j for j in range(n)] for i in range(n)]
b = [[i * j for j in range(n)] for i in range(n)]


def multiply(i):
    return [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]


def multiply(i):
    return [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]


if __name__ == "__main__":

    print("\nMatrix A")
    for row in a:
        print(row)

    print("\nMatrix B")
    for row in b:
        print(row)

    t1 = time.time()
    seq = [multiply(i) for i in range(n)]

    print("\nMatrix Result")
    for row in seq:
        print(row)

    print(f"Time taken by sequencial {time.time() - t1}")

    t2 = time.time()

    with multiprocessing.Pool() as p:
        result = p.map(multiply, range(n))

    print("\nMatrix Result")
    for row in result:
        print(row)

    print(f"Time taken by parallel {time.time() - t2}")
