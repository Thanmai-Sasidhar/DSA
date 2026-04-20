'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None

def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode

def delete(value):
    global head
    temp=head
    if temp and temp.data==value:
        head=temp.next
        return
    prev=None
    while temp and temp.data!=value:
        prev=temp
        temp=temp.next
    if temp is None:
        print("Value not in linkedlist......😭")
        return
    prev.next=temp.next
    print("Deleted value:",value)

def display():
    temp=head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("None")

n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)

print("Inserted linkedlist:")
display()
key=int(input("Enter the value of node to be deleted"))
delete(key)
print("\n Updated Linkedlist:")
display()
'''



'''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None

def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode

def delete(value):
    global head
    temp=head
    if temp and temp.data==value:
        head=temp.next
        return
    prev=None
    while temp and temp.data!=value:
        prev=temp
        temp=temp.next
    if temp is None:
        print("Value not in linkedlist......😭")
        return
    prev.next=temp.next
    print("Deleted value:",value)

def display():
    temp=head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("None")

#For Searching
def search(key):
    temp=head
    position=1
    while temp:
        if temp.data==key:
            print(f"Element found in node {position}")
            return
        temp=temp.next
        position+=1
    print("No Node reflects the key ")    

#Reverse the Linked List

def reverse():
    global head
    prev=None
    curr=head
    while curr:
        nextnode=curr.next
        curr.next=prev
        prev=curr
        curr=nextnode
    head=prev    
    

n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)

print("Inserted linkedlist:")
display()
reverse()
print("Reversed Linked Kist")
display()

'''

#Cycle detection TESTING

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None

def create_cycle(pos):
    global head
    if pos==-1:
        return 
    temp=head
    cycle_node=None
    index=0
    while temp.next:
        if index==pos:
            cycle_node=temp
        temp=temp.next
        if cycle_node:
            temp.next=cycle_node
            
def detect_cycle(pos):
    slow=head
    fast=head
    
    if pos==-1:
        return 
    temp=head
    cycle_node=None
    
                    
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode

def display():
    temp=head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("None")


n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)

print("Inserted linkedlist:")
display()



