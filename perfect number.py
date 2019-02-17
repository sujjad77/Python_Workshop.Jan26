def perfect(num):
    sum = 0
    for each in range(1, num):
        if num % each == 0:
            sum += each
    return sum == num

n=int(input("Enter a number:"))
print(perfect(n))


