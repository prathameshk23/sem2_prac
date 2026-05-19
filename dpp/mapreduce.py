from pyspark import SparkContext


def local_wc():
    t = open("input.txt").read().lower().split()
    print({w: t.count(w) for w in set(t)})


def spark():
    sc = SparkContext("local[*]", "WC")
    print(
        sc.textFile("input.txt")
        .flatMap(lambda x: x.split())
        .map(lambda x: (x.lower(), 1))
        .reduceByKey(lambda a, b: a + b)
        .collect()
    )


local_wc() if input("Choose 1:Local or 2: PySpark") == "1" else spark()
