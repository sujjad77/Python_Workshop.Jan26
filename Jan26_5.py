#Q5. Write a function called nested_sum that takes a list of lists of integers and adds up
#the elements from all of the nested lists. For example:
#>>> t = [[1, 2], [3], [4, 5, 6]]
#>>> nested_sum(t)
#21

def nested_sum(ll):
    _sum = 0
    for each in ll:
        _sum += sum(each)

    return _sum


t = [[1,2], [3], [4,5,6]]
s = nested_sum(t)
print("The sum is:",s)

""" OR CAN USE THIS METHOD TOO
for each in ll:
    for x in each:
        _sum += x
"""