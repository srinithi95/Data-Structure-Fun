#Basic python program for basic Linked List functions.
#Each node in the linked list
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

#LinkedList
class LinkedList:
    def __init__(self):
        self.head=None
    
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.val)
            temp=temp.next

#To insert a node in the begining of the Linked List
    def insertInTheBeginning(self,val):
        new_node=Node(val)
        if(self.head==None):
            self.head=new_node
            return

        new_node.next=self.head
        self.head=new_node

#To insert a node in the end of Linked List
    def insertInTheEnd(self,val):
        new_node=Node(val)
        if(self.head==None):
            self.head=new_node
            return

        last=self.head
        while(last.next):
            last=last.next
        
        last.next=new_node
        new_node.next=None

#To insert a node after a particular node
    def insertAfter(self,prev_node,val):
        new_node=Node(val)
        if(prev_node==None):
            print("previous node is NULL")
        
        new_node.next=prev_node.next
        prev_node.next=new_node

#To delete the Linked list
    def deleteNode(self,delval):
        temp=self.head
        if(temp==None):
            print("The Linked List does not exists")
            return
        
        if(temp.val==delval):
            self.head=temp.next
            temp=None
            return

        while(temp.val!=delval):
            prev=temp
            temp=temp.next

        prev.next=temp.next
        temp=None
    
    #remove duplicates from the linked list with temporary buffer
    def removeDuplicatesBuffer(self):

        buffer=[]
        current=self.head
        prev=current
        while(current!=None):

            if(current.val in buffer):
                prev.next=current.next
            else:
                prev=current
                buffer.append(current.val)
            current=current.next

    #remove duplicates from the linked list without temporary buffer

    def removeDuplicates(self):

        current=self.head

        while(current):
            runner=current
            while(runner.next):
                if(runner.next.val==current.val):
                    runner.next=runner.next.next
                else:
                    runner=runner.next

            current=current.next

 #algorithm to implement the kth to last element of the linked list

    def kthlastelement(self,k):
        first=self.head
        second=self.head
        i=0
        while(i<k):
            second=second.next
            i=i+1

        while(second):
            first=first.next
            second=second.next

        return first.val

if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
   
    # Insert 6.  So linked list becomes 6->None 
   
    print('here')
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.insertInTheBeginning(7); 
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.insertInTheBeginning(1); 
    print('here')
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.insertInTheEnd(4) 
    print('here')
    llist.insertInTheEnd(6) 
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(llist.head.next, 8) 
    llist.insertAfter(llist.head.next, 2) 
    llist.insertAfter(llist.head.next, 9) 

    llist.deleteNode(1)
    print ('Created linked list is:')
    llist.printList()
    #llist.removeDuplicates()
  
    print ('After removing duplicates:')
    print(llist.kthlastelement(3))
    #llist.printList()

    

    

        
        


       

        
   
   



    

    

