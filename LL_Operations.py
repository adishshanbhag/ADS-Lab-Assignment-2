from Question_1 import *

class LinkedListOperations(singleLinkedList):
    def __init__(self):
        super().__init__()

    def split_LinkedList(self):
        if not self.is_empty():
            # self.reverse_LinkedList()
            L1, L2 = singleLinkedList()
            curNode = self.head
            NodeCount=0
            while curNode!=None:
                if NodeCount%2 == 0:
                    L1.add_at_tail(curNode.data)
                else:
                    L2.add_at_tail(curNode.data)
            print("After splitting:")
            print("First Lin")
    def reverse_LinkedList(self):
        if not self.is_empty():
            curNode = self.head
            nextNode = curNode
            prevNode = None
            while nextNode!=None:
                nextNode = curNode.next
                curNode.next = prevNode
                prevNode = curNode
                curNode = nextNode
            self.head, self.tail = self.tail, self.head
    
    def sum_n_last_elements(self,n):
        if self.is_empty():
            print("No elements to delete")
        elif n<=0:
            print("n value cannot be less than 1")
        else:
            sum_start_ind =self.get_count()-n
            curNode = self.head
            node_count = 0
            sum = 0
            while curNode!=None:
                if node_count >= sum_start_ind:
                    sum+=curNode.data
                node_count+=1
                curNode = curNode.next
            return sum
        
    

            