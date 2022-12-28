def count_leaves(tree):
    if not tree:
        return 0
    elif isinstance(tree, int):
        return 1
    else:
        return count_leaves(tree[0]) + count_leaves(tree[1:])

tree = [[1, 2], 3, 4]
print(count_leaves(tree)) # 4


def scale_tree(tree, factor):
    if not tree:
        return []
    if isinstance(tree, int):
        return tree * factor
    else:
        return [scale_tree(tree[0], factor)] + scale_tree(tree[1:], factor)

tree = [1, [2, [3, 4], 5], [6, 7]]
print(scale_tree(tree, 10))
# [10, [20, [30, 40], 50], [60, 70]]


def scale_tree(tree, factor):
    return list(map(lambda sub_tree: scale_tree(sub_tree, factor)
                    if isinstance(sub_tree, list)
                    else sub_tree * factor, tree))
tree = [1, [2, [3, 4], 5], [6, 7]]
print(scale_tree(tree, 10))
# [10, [20, [30, 40], 50], [60, 70]]


def my_map(proc, items):
    if items == []:
        return []
    else:
        return [proc(items[0])] + my_map(proc, items[1:])