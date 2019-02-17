def middle(_list):
    _list2 = []
    for each in _list:
        if (each != _list[0] and each != _list[len(_list)-1]):
            _list2.append(each)
    return(_list2)


t = [1,2,3,4]
x = middle(t)
print("The final list is {}".format(x))