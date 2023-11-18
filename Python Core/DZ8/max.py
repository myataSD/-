def maximum(list, _max_ = None):
    if _max_ is None:
        _max_ = list.pop()
    current = list.pop()
    if  current  > _max_:
        _max_ = current
    if  list:
        return maximum(list, _max_)
    return _max_

    
    
print(maximum([5,1,7,3,-4,8,11]))
