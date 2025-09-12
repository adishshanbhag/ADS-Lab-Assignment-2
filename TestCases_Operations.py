from Question_1 import *
from LL_Operations import *

LL = LinkedListOperations()

def add_elements():
    LL.add_at_tail(20)
    LL.add_at_tail(40)
    LL.add_at_tail(60)
    LL.add_at_tail(80)
    LL.add_at_tail(100)
    LL.add_at_tail(120)

add_elements()
LL.reverse_LinkedList()
assert LL.sum_n_last_elements(3) == 120
print("Reversed Linked List: ")
LL.displayLL()
# n = int(input("Enter the number of elements for which sum is required: "))
# sum = LL.sum_n_last_elements(n)
# assert sum == 300
# print("Sum of last {} elements is: {}".format(n,sum))

