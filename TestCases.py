from Assignment import *

#Add at head

SLL = singleLinkedList()
# print("Adding element at head:")
SLL.add_at_head(10)
# assert SLL.get_count()==1

# print("\nBefore adding element:")
# SLL.displayLL()
# print("\n")
SLL.add_after_data(10,20)
SLL.add_after_data(20,30)
SLL.add_after_data(30,40)
# print("After adding element")
# SLL.displayLL()
# print("\n")

#add at tail

# print("Adding element at tail")
# print("LL before adding element")
# SLL.displayLL()
SLL.add_at_tail(50)
# assert SLL.get_count()==5
# print("LL after adding element")
# SLL.displayLL()

#delete head and tail
# print("Before deleting the element:")
# SLL.displayLL()
# SLL.delete_tail()
# assert SLL.get_count()== 4 #4
# print("\nElement deleted")
# SLL.displayLL()

# print("Before deleting the element:")
SLL.displayLL()
if  SLL.search_Element(30) :
    print("element found")
# print("\nElement Deleted")
# SLL.disgplayLL()
