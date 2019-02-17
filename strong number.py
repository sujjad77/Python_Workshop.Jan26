def  strong(num):
    sum = 0
    for i in (num, num//10, (num//10)//10):
        fact = 1
        j = i % 10
        for each in range(1, j+1):
            fact = fact*each
        sum += fact
    print(sum)
    return sum == num


print(strong(145))



