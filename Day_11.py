#Searchings in Array 

#1.Linear Search 

'''
---It is a simple technique where you check element one by one until you reach the target

Algo:

1.Start with index 0

2.Compare each elemnet with the target 

3.If it matchhes then return target 

4.else move to next element 

5.If reaches end then the element not found


#BEST CASE --> O(1)

#WORST CASE  --> O(n)
'''

#CODE
'''
arr=list(map(int,input().split()))
target=int(input("Enter element to be searched: "))
found=False

if target not in arr:
    print("Target not in List...")
else:
    for i in range(len(arr)):
            if arr[i]==target:
                print(f"Element found at index {i}")
                found = True
                break
if not found:
            print("Element not found...!")    
'''

#2.BINARY SEARCH
'''
Algo:

1.We will take 2 pointers low=0 and high=n-1

2.mid=(low+high)//2

3.Compare if arr[mid]==target 
          if arr[mid]<arr[mid] --> Search left side
          if arr[mid]>arr[mid] --> Search right side
 
4.Repeat until low=high=mid

a=[5,4,17,23,25,45,59,63,71,89]
   |                         |
   |                         |
   left                     right
   
target=59
mid=(0+9)//2 --> floor(4.5)-->4

'''
#CODE
'''
arr=list(map(int,input().split()))
arr.sort()
found=False
target=int(input("Enter the element to be searched: "))
left=0
right=len(arr)-1

while left<=right:
    mid =(left+right)//2
    if arr[mid]==target:
        print(f"Element found at index {mid}")
        found=True
        break
    elif arr[mid]<target:
        right=mid-1
    else:
        left=mid+1
if not found:
    print("Element not Found..")            
'''

#DRY RUN
'''
2 4 6 8 10 12
10

l=0 r=5
while 0<=5
mid=l+r//2 --> 2

arr[2]==6 
as arr[mid]<target
    6<10
    left+=1 --> 3
    
while 3<=5
l=3
r=5
m=4
arr[4]==10    
    10==10 #True 

'''
#3.Jump Search

'''
-- Works in sorted arrays only 

--some what better than linear search

arr=[2 4 6 8 10 12 14 16 18]
     0 1 2 3 4  5  6  7  8 
    [2 4 6      8 10 12     14 16 18]
     0          3           6   

time complexity : root(n)

target = 16
checks 

arr[0]==target --> 2==16
arr[3]==target --> 8==16
arr[6]==target --> 14==16

Then initialise the i+=1

arr[1]==target --> 4==16
arr[4]==target --> 10==16
arr[7]==target --> 16==16 #True
'''
'''
Algo:

1.choose step size --> Square root(n)

2.jump for all divided steps 

3.stop 
       when element is greater (or) reaches the end of array  
'''


#CODE
import math as m
arr=list(map(int,input().split()))
target =int(input())
n=len(arr)
step=int(m.sqrt(n))
i=0
while i<n and arr[min(i+step,n)-1]<target:
    i+=step
for j in range(i,min(i+step,n)):
    if arr[j]==target:
        print(f"Found at index {i}")
        break
else:
    print("Not Found...! ")        
    
















