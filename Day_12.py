#Sortings

#Bubble Sort   
'''
if Adjacent value sorting where arr[0]>arr[i+1] --> Perform swap

else arr[0]!>arr[i+1] --> increment or pass to next element

Here Right most highest element will be sorted first

Algo:

1.Start index

2.Read array of size n 

3.for each pass compare adjacent elements 
        repeat for 0 to n-1 times
        
4.for j 0 - > n-i-2:
    swap(a[j]),a[j+1])
    
5.After each pass largest elemnet moves to end 

6.Repeat pass till all the elements are sorted            
'''

#CODE
'''
arr=list(map(int,input("Enter elements: ").split()))
n=len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted array: ",arr)                    
'''

#DRY RUN
''''
arr=[5,3,8,4,2]

n=5
i=0
    j=0 to 3
    j=0
    arr[0]>arr[1]
        5>3 swap
                        #3 5 8 2 4
    j=1
    arr[1]>arr2
        5>8 False
    j=2
    arr[2]>arr[3]
        8>4 True
        swap
                        #3 5 4 8 2
    j=3
    arr[3]>arr[4]
        8>2
        swap            #3 5 4 2 8
     
i=1
    j=0 to 2
    j=0
    arr[0]>arr[1]
        3>5 swap
    arr[1]>arr[2]
        5>4 swap        #3 4 5 2 8
    j=1
    arr[2]>arr[3]
        5>2 swap        #3 4 2 5 8
    j=2
    arr[3]>arr[3]
        5>8 False       #3 4 2 5 8
i=2
    j=0 to 1
    j=0
    arr[0]>arr[1]
        3>4 False       #3 4 2 5 8
    arr[1]>arr[2]
        4>2 swap.       #3 2 4 5 8        
    j=1
    arr[2]>arr[3]
        4>5 swap        #3 2 4 5 8
     
i=3
    j=0 to 0
    j=0
    arr[0]>arr[1]
        3>2
        swap          #2 3 4 5 8     
'''

#Selection sort
'''
Algo:
1.Start from index 0

2.Assume current position is minimum

3.search the rest of the array to find the actual minimum

for i:0 to n-1
    min_index=0
    for j :i+1 to n-1
    if arr[j]<arr[min_index]

4.swap arr[i] and arr[min_index]

5.repeat till the last index

'''
#CODE 1
'''
arr=list(map(int,input().split()))
n=len(arr)
i=0
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j # or else we can remove this and place j in the above and have to place the below line inside the for loop 
        arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)   
'''

#DRY RUN
'''
[4,3,2,1]
4

i=0
for 0 to 3
    min_index=0
    for 1 to 3
    j=1
    arr[1]<arr[min_index]
        3<4 True
        min_index=1 
        swap                    #3 4 2 1
    j=2
    arr[2]<arr[min_index]
        2<3 True
        min_index=2
        swap                    #3 2 4 1
    j=3    
        
    arr[i],

'''         
            
#CODE 2(ME)
'''
arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    for j in range(n):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            continue
print(arr)            
'''            



