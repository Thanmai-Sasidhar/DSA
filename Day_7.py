#Array operations
'''
1.traversal operation

2.insertion operation-->diffference bw insert update 

3.deletion -->pop and remove

4.update 

5.sorting --> ascending and descending order
'''

#traversal operations
'''
a=[4,5,6,9,8]
for i in a:
    print(i)
'''
#append operation (Faster than insert)
'''
arr=[1,2,3,4,5,6,7,8]
print("Before append : ",arr)
arr.append(9)
print("After append : ",arr)
'''
#insert operation 
'''
arr=[1,2,3,4,5]
print("Before insert:",arr)
arr.insert(2,10)
print("After insertion:",arr)
'''
#insertion of Numbers
'''
n=int(input("Enter the number"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the {i+1} element :")))
print("Before insertion",arr)
arr.insert(int(input("Enter the index position: ")),int(input("Enter the value: ")))
print(arr)
'''
'''
arr=list(map(int,input().split()))
print("Before insert:",arr)
arr.insert(int(input()),int(input()))
print("After insert :",arr)
'''
#Insertion of characters
'''
n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    arr.append(input(f"Enter the {i+1} element :"))
print("Before insertion",arr)
arr.insert(int(input("Enter the index position: ")),input("Enter the value: "))
print("After insertion :",arr)
'''
'''
arr=list(map(str,input().split()))
print("Before insert:",arr)
arr.insert(int(input("Enter the index position: ")),input("Enter the value of character: "))
print("After insert :",arr)
'''

#Delete Operations(delete--takes index value , pop--takes index value, remove-- takes value)
#pop --> traversing directly to index value
'''
arr=[1,2,5,3,4]
print("Before popping: ",arr)
arr.pop(2)
print("After popping : ",arr)
'''
#delete del -->Traversing node by node
'''
arr=[1,2,3,4,5]
n=int(input("Enter the number"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter the {i+1} element :")))
    
print("Before insertion",arr)
arr.insert(int(input("Enter the index position: ")),int(input("Enter the value: ")))
print(arr)del arr[4]
print("After Deletion :",arr)
'''
#remove --> 
'''
arr=[1,2,3,4,5,6]
print("Before insertion",arr)
arr.remove(3)
print("After Removing :",arr)
'''

#Using user input
'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element")))
print("Before removing : ",arr)
value=int(input("Enter the value: "))
arr.remove(value)
print("After removing: ",arr)
'''
'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input("Enter the element")))
print("Before removing : ",arr)
val=int(input("Enter the value to remove:"))
arr.pop(arr.index(val))
print("After deletion",arr)    
'''

#update vs replace

#Manual replacing
'''
arr=[1,2,3,3,5,6]
arr[3]=4
print(arr)      
'''
#Dynamic manual
'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
index=int(input())
val=int(input())
arr[index]=val
print("After : ",arr)    
'''

#SORTING
'''
arr=[1,2,3,4,5]
print("Before Reversing: ",arr)
arr.sort(reverse=True)
print("After Reversing:",arr)
'''    
    
