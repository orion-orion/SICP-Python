# 集合作为未排序的表
def is_element_of_set(x, set):
    if not set:
        return False
    elif x == set[0]:
        return True
    else:
        return is_element_of_set(x, set[1: ]) 
    
def adjoin_set(x, set):
    if is_element_of_set(x, set):
        return set
    else:
        return [x] + set

def intersection_set(set1, set2):
    if not set1 or not set2:
        return []
    elif is_element_of_set(set1[0], set2):
        return [set1[0]] + intersection_set(set1[1: ], set2)
    else:
        return intersection_set(set1[1: ], set2)

set1, set2 = [10, 5, 2], [6, 7, 5] 
print(is_element_of_set(5, set1)) # True
print(is_element_of_set(99, set1)) # False
print(adjoin_set(11, set1)) # [11, 10, 5, 2]
print(intersection_set(set1, set2)) # [5]


# 集合作为排序的表
def is_element_of_set(x, set):
    if not set:
        return False
    elif x == set[0]:
        return True
    elif x < set[0]:
        return False
    else:
        return is_element_of_set(x, set[1: ]) 

def intersection_set(set1, set2):
    if not set1 or not set2:
        return []
    else:
        x1, x2 = set1[0], set2[0]
        if x1 == x2:
            return [x1] + intersection_set(set1[1:], set2[1: ])
        elif x1 < x2:
            return intersection_set(set1[1: ], set2)
        elif x2 < x1:
            return intersection_set(set1, set2[1: ])

set1, set2 = [2, 5, 10], [5, 6, 7] 
print(is_element_of_set(5, set1)) # True
print(is_element_of_set(99, set1)) # False
print(adjoin_set(11, set1)) # [11, 2, 5, 10]
print(intersection_set(set1, set2)) # [5]