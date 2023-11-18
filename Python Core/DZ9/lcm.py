a = int(input())
b = int(input())

multiplication_of_a_b = a * b

# Нахождение НОД
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else: 
        b = b % a
gcd = a + b

# Нахождение НОК
lcm = multiplication_of_a_b / gcd
print(lcm)