#Doubly Linked List
'''
1.Insert at begin

2.Insert at end 

3.Insert at position

4.Delete from beginning

5.Delete from end

6.Delete by value

7.Search an element

8.Reverse a DLL

9.Replace

10.Display forward and backward traversal
'''

class node:
    def __init__(self,data): #Creates Data,prev,next
        self.data=data
        self.next=None
        self.prev=None
        
def insert_at_begin(head,data): #Inserts from begin point onlyy 
    newnode=node(data)
    if head:
        head.prev=newnode
        newnode.next=head
    return newnode

def insert_at_end(head,data):
    newnode=node(data)
    if head is None:
        return newnode
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=newnode
    newnode.prev=temp    
    return head    

def insert_at_position(head,data,pos):
    newnode=node(data)
    if pos==1:
        if head:
            head.prev=newnode
            newnode.next=head
        return newnode
    temp=head
    for _ in range(pos-2):
        if temp is None:
            return head
        temp=temp.next
    
    if temp is None:
        return head
    newnode.next=temp.next

    if temp.next:
        temp.next.prev=newnode

    temp.next=newnode
    newnode.prev=temp
    return head      

def delete_begin(head):
    if head is None:
        return None
    head=head.next
    if head:
        head.prev=None
    return head
    
def delete_from_end(head):
    if head is None:
        return None
    temp=head
    if temp.next is None:
        return None
    while temp.next:
        temp=temp.next
    temp.prev.next=None
    return head

def display(head): #To display the Nodes
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")
    
head = None
n = int(input("Enter the no of nodes: "))

for i in range(n):
    val = int(input("Enter the value: "))
    head = insert_at_position(head, val, i + 1)

# pos = int(input("Enter position to insert: "))
# val = int(input("Enter value to insert: "))
# head = insert_at_position(head, val, pos)

head=delete_from_end(head)
display(head)