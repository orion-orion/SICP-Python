class LinkedList():
    def __init__(self, *items) -> None:
        """提供两种初始化方式:序对或多个元素
        """
        if isinstance(items[0], list):
            self.pair = items[0]
        else:
            self.pair = self._construct(*items)

    def _construct(self, *items):
        """递归地构造链表
        """
        if items == ():
            return None
        else:
            item, *rest = items
            return [item, self._construct(*rest)]

    def __repr__(self):
        """重写打印函数
        """
        return "-->".join(map(str, self._flatten(self.pair)))

    def _flatten(self, pair):
        """遍历链表，返回其一维展开
        """
        if pair is None:
            return []
        else:
            return [pair[0]] + self._flatten(pair[1])

    @property
    def head(self):
        """获取链表头部元素
        """
        return self.pair[0]

    @property
    def rest(self):
        """获取链表头部元素之外的元素，并以链表形式返回
        """
        if self.pair[1] is None:
            return None
        else:
            return LinkedList(self.pair[1])

print(LinkedList(1, 2, 3, 4))
# 1-->2-->3-->4


def list_ref(items, n):
    if n == 0:
        return items.head
    else:
        return list_ref(items.rest, n-1)

print(list_ref(LinkedList(1, 4, 9, 16, 25), 3))  # 16


def length(items):
    if items is None:
        return 0
    else:
        return 1 + length(items.rest)

print(length(LinkedList(1, 3, 5, 7)))  # 4


# 以迭代的方式计算lengths(尾递归)
def length(items):
    def length_iter(a, count):
        if a is None:
            return count
        else:
            return length_iter(a.rest, count + 1)
    return length_iter(items, 0)

print(length(LinkedList(1, 3, 5, 7)))  # 4


def append(lk_list1, lk_list2):
    if lk_list1 is None:
        return lk_list2.pair
    else:
        return [lk_list1.head, append(lk_list1.rest, lk_list2)]

odds = LinkedList(1, 3, 5, 7)
squares = LinkedList(1, 4, 9, 16, 25)
print(LinkedList(append(odds, squares)))  # 1-->3-->5-->7-->1-->4-->9-->16-->25
print(LinkedList(append(squares, odds)))  # 1-->4-->9-->16-->25-->1-->3-->5-->7


def scale_list(items, factor):
    if items is None:
        return None
    else:
        return [items.head * factor, scale_list(items.rest, factor)]

print(LinkedList(scale_list(LinkedList(1, 2, 3, 4, 5), 10)))
# 10-->20-->30-->40-->50


def my_map(proc, items):
    if items is None:
        return None
    else:
        return [proc(items.head), my_map(proc, items.rest)]

print(LinkedList(my_map(abs, LinkedList(-10, 2.5, -11.6, 17))))
# 10-->2.5-->11.6-->17
print(LinkedList(my_map(lambda x: x**2, LinkedList(1, 2, 3, 4, 5))))
# 1-->4-->9-->16-->25


def scale_list(items, factor):
    return LinkedList(my_map(lambda x: x*factor, items))

print(scale_list(LinkedList(1, 2, 3, 4, 5), 10))
# 10-->20-->30-->40-->50
