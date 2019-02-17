"""Q6. Write a function called cumulative_sum that takes a list of numbers and returns the cumulative
sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cum_sum(t)
[1, 3, 6]"""



def cum_sum(ll):
    _sum = 0
    _list = []
    for each in ll:
        _sum += each
        _list.append(_sum)

    return _list


t = [1,2,3]
s = cum_sum(t)
print("The sum is:",s)

