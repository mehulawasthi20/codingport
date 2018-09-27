     

class Node:
    def __init__(self, data):
        #self.head = None
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    
            

           
    
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #llist = self.driver()
        curr = self.head
        
        if (curr is not None): 
            if (curr.val == node): 
                self.head = curr.next
                node = None
                return
        
        while curr != None:
            if curr.val == node:
                break
            prev = curr
            curr = curr.next
            
        if curr == None:
            print("Node value not in list")
        
        else:
            prev.next = curr.next
            curr = None
        
    def print(self):
        curr = self.head
        while curr != None:
            print (" %d" %(curr.val))
            curr = curr.next
        
        


llist = LinkedList()
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(7)
llist.push(9)
llist.deleteNode(5)
llist.print()

