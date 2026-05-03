'''
(rear+1)%n==front

if full --> overflow

if queue is empty (front==-1)

front =rear =0

insertion.      front.        rear.            queue


 
'''
#Circular Queue
class circularqueue:
    
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1

    def is_empty(self):
        return self.front==-1
    
    def is_full(self):
        return (self.rear+1)%self.size==self.front
    
    def enqueue(self,value):
        if self.is_full():
            print("Queue Overflow, cannot insert", value)
            return 
        
        if self.is_empty():
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.size
        
        self.queue[self.rear]=value
        print("Inserted:", value)
        
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return 
        
        removed=self.queue[self.front]
        
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size   # ✅ FIXED
        
        print("Deleted:", removed)
        
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front Element:", self.queue[self.front])
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        i = self.front
        print("Queue elements:", end=" ")
        
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


# -------- MAIN PROGRAM --------
size=int(input("Enter size: "))
cq=circularqueue(size)

while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
    choice=int(input("Enter choice: "))
    
    if choice==1:
        val=int(input("Enter value: "))
        cq.enqueue(val)
        
    elif choice==2:
        cq.dequeue()
        
    elif choice==3:
        cq.peek()
        
    elif choice==4:
        cq.display()
        
    elif choice==5:
        print("Exiting...")
        break
        
    else:
        print("Invalid choice")                
        
