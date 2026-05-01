#Enqueue
'''
queue=[]
n=int(input("Enter the size of queue: "))
for i in range(n):
    val=int(input("Enter the value : "))
    queue.append(val)
print("Queue after Enqueue: ",queue)    
'''


#Dequeue
''' 
queue=list(map(int,input().split()))
if len(queue)==0:
    print("Queue is Empty...")
else:
    removed=queue.pop(0)  
    print("Dequeued Element :",removed)
    print("Remaining Elements : ",queue)
    print("Peek Element: ",queue[0])
    print("Size of Queue :",len(queue))
'''

#Enqueue using Linked List 
'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None    
        
front=rear=None
n=int(input("Enter the no of Elements: "))
for i in range(n):  
    val=int(input("Enter the Value: "))
    new=node(val)
    if front is None:
        front=rear=new
    else:
        rear.next=new
        rear=new
        
temp=front
print("Queue after enqueue :",end=" ")
while temp:
    print(temp.data,end=" ")
    temp=temp.next                  
'''    


#Dequeue using Linked List

'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None    
        
front=rear=None
n=int(input("Enter the no of Elements: "))
for i in range(n):  
    val=int(input("Enter the Value: "))
    new=node(val)
    if front is None:
        front=rear=new
    else:
        rear.next=new
        rear=new

if front is None:
    print("Queue is Empty...")
else:
    removed=front.data
    front=front.next
    if front is None:
        rear=None
    print("Dequeued Element is : ",removed)    
        
temp=front
print("Queue after Dequeue :",end=" ")
while temp:
    print(temp.data,end=" ")
    temp=temp.next  
'''




       
