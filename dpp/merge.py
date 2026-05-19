from multiprocessing import Process, Queue


def merge(a, b):
    r = []
    while a and b:
        r.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    return r + a + b


def sort(a):
    mid = len(a) // 2
    return a if len(a) <= 1 else merge(sort(a[:mid]), sort(a[mid:]))


def parallel_sort(a, q):
    q.put(sort(a))


if __name__ == "__main__":
    arr = [8, 3, 7, 4, 9, 2, 6, 5]
    mid = len(arr) // 2
    q1, q2 = Queue(), Queue()

    p1 = Process(target=parallel_sort, args=(arr[:mid], q1))
    p2 = Process(target=parallel_sort, args=(arr[mid:], q2))

    p1.start()
    p2.start()

    sorted_arr = merge(q1.get(), q2.get())

    p1.join()
    p2.join()

    print("Unsorted:", arr)
    print("Sorted:", sorted_arr)
