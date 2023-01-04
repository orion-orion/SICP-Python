def make_leaf(symbol, weight):
    return ["leaf", symbol, weight]

def is_leaf(object):
    return object[0] == "leaf"

def symbol_leaf(x):
    return x[1]

def weight_leaf(x):
    return x[2]

def make_code_tree(left, right):
    return [left, \
            right, \
            symbols(left) + symbols(right), \
            weight(left) + weight(right)]

def left_branch(tree):
    return tree[0]

def right_branch(tree):
    return tree[1]

def symbols(tree):
    if is_leaf(tree):
        return symbol_leaf(tree)
    else:
        return tree[2]
    
def weight(tree):
    if is_leaf(tree):
        return weight_leaf(tree)
    else:
        return tree[3]

def decode(bits, tree):
    def decode_1(bits, current_branch):
        if not bits:
            return ""
        else:
            next_branch = choose_branch(bits[0], current_branch)
            if is_leaf(next_branch):
                return symbol_leaf(next_branch) + decode_1(bits[1: ], tree)
            else:
                return decode_1(bits[1: ], next_branch)                
    return decode_1(bits, tree)

def choose_branch(bit, branch):
    if bit == "0":
        return left_branch(branch)
    elif bit == "1":
        return right_branch(branch)
    else:
        raise ValueError("error: bad bit -- CHOOSE-BRANCH %s" % bit)

        
sample_tree = make_code_tree(make_leaf("A", 4),  
                             make_code_tree(
                                 make_leaf("B", 2),
                                 make_code_tree(make_leaf("D", 1), make_leaf("C", 1))
                             ))
print(sample_tree)
# [['leaf', 'A', 4], [['leaf', 'B', 2], [['leaf', 'D', 1], ['leaf', 'C', 1], 'DC', 2], 'BDC', 4], 'ABDC', 8]
sample_message = "0110010101110"
decoded_message = decode(sample_message, sample_tree)
print(decoded_message)
# ADABBCA


def encode(message, tree):
    if not message:
        return ""
    else:
       return encode_symbol(message[0], tree) + encode(message[1:], tree)
    
def encode_symbol(symbol, current_branch):
    if is_leaf(current_branch):
        return ""
    else:
        left, right = left_branch(current_branch), right_branch(current_branch)
        if symbol in symbols(left):
            return "0" + encode_symbol(symbol, left)
        elif symbol in symbols(right):
            return "1" + encode_symbol(symbol, right)
        else:
            raise ValueError("error: bad symbol -- CHOOSE-BRANCH %s" % symbol)

sample_message = "ADABBCA"
encoded_message = encode(sample_message, sample_tree)
print(encoded_message)
# 0110010101110


def generate_huffman_tree(paris):
    return successive_merge(make_leaf_set(paris))

def make_leaf_set(pairs):
    if not pairs:
        return []
    else:
        pair = pairs[0]
        return adjoin_set(make_leaf(pair[0], pair[1]), \
                          make_leaf_set(pairs[1: ]))
        
def successive_merge(leaf_set):
    if len(leaf_set) == 1:
        return leaf_set[0]
    left, right = leaf_set[0], leaf_set[1]
    return successive_merge(adjoin_set(make_code_tree(left, right), leaf_set[2: ]))
    
def adjoin_set(x, set):
    if not set:
        return [x]
    if weight(x) < weight(set[0]):
        return [x] + set 
    else:
        return [set[0]] + adjoin_set(x, set[1: ])
        

pairs = ([("A", 4), ("B", 2), ("D", 1), ("C", 1)])
tree = generate_huffman_tree(pairs)
print(tree)
# [['leaf', 'A', 4], [['leaf', 'B', 2], [['leaf', 'C', 1], ['leaf', 'D', 1], 'CD', 2], 'BCD', 4], 'ABCD', 8]
