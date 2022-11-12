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


def lab_3():
    words = input("Enter words (a,b,c,d ...): ").split(",")
    print(*[word for word in words if word[0] in word[1:]])


def lab_4():
    from random import randint
    matrix = []
    n, m = 5, 6
    for i in range(n):
        matrix.append([randint(0, 9) for j in range(m)])

    for row in matrix:
        print(*row)

    lst = [el for row in matrix for el in row]
    print(f"max count element: {max(lst, key=lambda el: lst.count(el))}")
    # якщо є декілька елементів які появляються найбільшу кількість раз
    # то серед них буде обрано менший з цих елементів за значенням
