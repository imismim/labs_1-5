def lab_1():
    a, n = list(map(int, input("Enter a n: ").split(" ")))
    result = 1
    for i in range(0, n + 1):
        result *= a - i * n

    print(f"Result: {result}")


def lab_2():
    numbers = list(map(int, input("Enter numbers: ").split(" ")))
    numbers_count = sorted([[number, numbers.count(number)] for number in set(numbers)], key=lambda x: x[1],
                           reverse=True)
    numbers_same_count = sorted([number for number in numbers_count if number[1] == numbers_count[0][1]])
    print(f"the most common: {numbers_same_count[0][0]}")
