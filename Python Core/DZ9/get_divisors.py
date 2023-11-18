def get_all_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

n =  int(input())

res = get_all_divisors(n)

print(list(res))