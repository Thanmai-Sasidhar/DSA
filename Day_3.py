#Taking the input in an array
'''
arr=[]
n=int(input("Enter the Length of the array: "))
for i in range(n):
    a=int(input(f"Enter the {i+1} value of array: "))
    arr.append(a)
print(arr)
'''

#Traversing in an array
#---Method 1
'''
arr=[1,2,3,4,5]
for i in arr:
    print(i,end=" ")
'''
#---Method 2
'''
arr=[6,7,8,9,10]
for i in range(len(arr)):
    print(arr[i],end=" ")
'''

#Sum of every element in an array
'''
sum=0
arr=[1,2,3,4,5,6]
for i in arr:
    sum+=i
print(sum)    
'''

#Largest Element in an array

#KEY POINT --> We should consider the 1st element as the Largest and compare with all other elements

'''
arr=[8,12,3,4,6]
large=arr[0]
for i in arr:
    if i>large:
        large=i
print(large)        
'''
