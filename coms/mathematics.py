def isprime(n):
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    maximum = n**0.5+1
    i = 3
    while i <= maximum:
        if n % i == 0:
            return 0
        i+=2
    return 1
