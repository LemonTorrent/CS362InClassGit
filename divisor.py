def divisors(num):
    arrDivisors = []

    for i in range(1, num):
        if (num % i == 0):
            arrDivisors.append(i)

    print("Array of divisors:", arrDivisors)

n = 100
divisors(n)
