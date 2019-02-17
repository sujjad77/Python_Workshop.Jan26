def sum_digits_sqr(n):
    a = n
    rem = 0
    sum = 0
    while a != 0:
        rem = a % 10
        sum += rem ** 2
        a /= 10
    return sum


n = int(input("Enter number: "))
a = n

while sum_digits_sqr(n) != 1:
    n = sum_digits_sqr(n)
    if sum_digits_sqr(n) == 1:
        print
        "Happy number"
        break
