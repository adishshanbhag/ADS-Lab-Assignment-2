from Assignment import *

SLL = singleLinkedList()
# print("Adding element at head:")
SLL.add_at_head(10)
# assert SLL.get_count()==1
# SLL.displayLL()

SLL.add_after_data(10,20)
SLL.add_after_data(20,30)
SLL.add_after_data(30,40)

# print("Adding element at tail")
# print("LL before adding element")
SLL.displayLL()
