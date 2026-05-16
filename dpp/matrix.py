import multiprocessing
import time

# Matrix size
SIZE = 3

# Initialize matrices
A = [[i + j for j in range(SIZE)] for i in range(SIZE)]
B = [[i * j for j in range(SIZE)] for i in range(SIZE)]


# Function to compute one row of result
def multiply_row(i):
    row = []
    for j in range(SIZE):
        sum_val = 0
        for k in range(SIZE):
            sum_val += A[i][k] * B[k][j]
        row.append(sum_val)
    return row


if __name__ == "__main__":

    # Sequential multiplication
    start_seq = time.time()

    seq_result = []
    for i in range(SIZE):
        seq_result.append(multiply_row(i))

    end_seq = time.time()

    print("\nSequential Time:", end_seq - start_seq)

    print("Matrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    start = time.time()

    # Create process pool
    with multiprocessing.Pool() as pool:
        result = pool.map(multiply_row, range(SIZE))

    end = time.time()

    # FIXED: These lines are now indented correctly
    print("\nResult Matrix C:")
    for row in result:
        print(row)
    print("\nParallel Time Taken:", end - start, "seconds")
