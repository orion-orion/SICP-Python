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


def entry(tree):
    return tree[0]

def left_branch(tree):
    return tree[1]

def right_branch(tree):
    return tree[2]

def make_tree(entry, left, right):
    return [entry, left, right]

def is_element_of_set(x, set):
    if not set:
        return False
    elif entry(set) == x:
        return True
    elif x < entry(set):
        return is_element_of_set(x, left_branch(set))
    elif x > entry(set):
        return is_element_of_set(x, right_branch(set))
    
set = [7, [3, [1, [], []], [5, [], []]], [9, [], [11, [], []]]]
print(is_element_of_set(5, set)) # True
print(is_element_of_set(99, set)) # False


def adjoin_set(x, set):
    if not set:
        return make_tree(x, [], [])
    elif x == entry(set):
        return set
    elif x < entry(set):
        return make_tree(entry(set), \
                        adjoin_set(x, left_branch(set)), \
                        right_branch(set))
    elif x > entry(set):
        return make_tree(entry(set), \
                        left_branch(set), \
                        adjoin_set(x, right_branch(set)))
        
set = [7, [3, [1, [], []], [5, [], []]], [9, [], [11, [], []]]]
print(adjoin_set(6, set))
# [7, [3, [1, [], []], [5, [], [6, [], []]]], [9, [], [11, [], []]]]


# def lookup(given_key, set_of_records):
#     if not set_of_records:
#         return False
#     elif given_key == key(set_of_records[0]):  
#         return set_of_records[0]
#     else:
#         return lookup(given_key, set_of_records[1: ])
    