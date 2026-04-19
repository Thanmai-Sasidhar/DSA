# Linked list

'''
1. Single Linked List

2.Double Linked list

3.Circular linked list 
'''

#Single Linked list
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("Enter the no of nodes:"))
head=None

for i in range(n):
    val=int(input("Enter the value: "))
    newnode=Node(val)
    if head==None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        
        
print("Linked List: ",end=" ")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print(None)    
'''
#Insert from an Beginning in single LL
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input("Enter the no of nodes:"))
head=None
                 
for i in range(n):
    val=int(input("Enter the value: "))
    newnode=Node(val)
    if head==None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
              
x=int(input("Enter the value to insert at beginning: "))
newnode=Node(x)
newnode.next=head
head=newnode        

print("Linked List: ",end=" ")
temp=head
while temp:
    print(temp.data,end="->")
    temp=temp.next
print(None)    
'''

#Insert from Beginning
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None
def insert_at_begin(data):
    global head
    newnode=Node(data)
    newnode.next=head
    head=newnode
            
n=int(input("Enter the no of Nodes: "))
for _ in range(n):
    val=int(input("Enter the Value: "))
    insert_at_begin(val)

temp=head

print("Linked List:")
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Tail")    
'''            
        
            
