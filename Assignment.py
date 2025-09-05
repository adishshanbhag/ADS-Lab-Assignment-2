class singleLinkedList:
    class _node_:
        def __init__(self, ele):
            self.data = ele
            self.next = None
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0
    
    def get_count(self):
        return self.count
    
    def displayLL(self):
        if self.is_empty():
            print("Linked list is empty")
        else:
            cur = self.head
            while cur!=None:
                print("{} ".format(cur.data), end=" ")
                cur = cur.next
    #add head element
    def add_at_head(self, ele):
        new_node = self._node_(ele)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count+=1

    #add tail element
    def add_at_tail(self,ele):
        new_node = self._node_(ele)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    
    #delete head
    def delete_head(self):
        if not self.is_empty():
            cur = self.head.next
            self.head.next = None
            del(self.head)
            self.head = cur
            self.count-=1
    
    #delete tail element
    def delete_tail(self):
        if not self.is_empty():
            cur = self.tail
            prev = self.head

            while prev.next!=cur :
                prev= prev.next
            prev.next = None
            del(cur)
            self.tail = prev
            self.count = self.count - 1

    #add element after data
    def add_after_data(self,key, ele):
        if not self.is_empty():
            cur = self.head
            while cur.data != key and cur!=None:
                cur = cur.next
            if cur!=None:
                new_node = self._node_(ele)
                new_node.next = cur.next
                cur.next = new_node
                if cur == self.tail:
                    self.tail = new_node
                self.count+=1
                print("Element {} added after {} Node".format(ele,key))
        else:
            print("Linked list is empty")
    
    #delete element after data
    def delete_after_data(self,key):
        if not self.is_empty():
            cur = self.head
            while cur.data!=key and cur!=None:
                cur = cur.next
            if cur!=None and cur.next!=None:
                temp = cur.next
                if self.tail == temp:
                    self.tail = cur
                cur.next = temp.next
                temp.next = None
                del(temp)
                self.count-=1
            else:
                print("No element to delete")
    
    #search element
    def search_Element(self,key):
        if not self.is_empty():
            temp = self.head
            while temp.data!=key and temp!=None:
                temp = temp.next
            if temp!=None:
                return temp.data
        return False
            
            
    







