def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for num in range(1, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

n = int(input("Введите число n: "))
prime_numbers = find_primes(n)
print("Простые числа от 1 до", n, ":", *prime_numbers)
