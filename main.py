def lab_1():
    a, n = list(map(int, input("Enter a n: ").split(" ")))
    result = 1
    for i in range(0, n + 1):
        result *= a - i * n

    print(f"Result: {result}")

