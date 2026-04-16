#Flip Sort

'''

Initial array 

[3, 6, 1, 5, 2, 4]

Find out the largset element -->6
if lagest is at top flip 

[6, 3, 1, 5, 2, 4]

after flip 
[4, 2, 5, 1, 3, 6]
Now the largest element is placed at last now we have to iterate upto n-i
Now identify large --> 5 
now make a flip from 0 to large 

after flip 
[5, 2, 4, 1, 3, 6]

now make a flip upto n-i(last but one as i=1)
[3, 1, 4, 2, 5, 6]

After flip
[4, 1, 3, 2, 5, 6]

As now the laregt value 4 in top make a flip from 0 to n-2

[2, 3, 1, 4, 5, 6]

as the loewst element is 1 make a flip 
[3, 2, 1, 4, 5, 6]

After flip
[1, 2, 3, 4, 5, 6]
'''

'''
#Approach 

1.Find max element in the unsorted array 

2.bring it to the zero index value followed by the respective values

3.then flip the total array to the correct position 
start from last index(n-1)

repeat
-flip index max(0->1)
-flip from 0->max_index
-flip 0 to i 

'''

#Program
'''
def flip(arr,k):
    start=0
    while start<k:
        arr[start],arr[k]=arr[k],arr[start]
        start+=1
        k-=1
        
def pancake(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        max_index=0
        for j in range(1,i+1):
            if arr[max_index]<arr[j]:
                max_index=j
        if max_index!=0:
            flip(arr,max_index)
        flip(arr,i)
    return arr

arr=list(map(int,input().split()))
sorted_array=pancake(arr)

print("Sorted array: ",sorted_array)
'''


'''
pass 1:

    i=5 -> position of largets element 
    
    max=6 index =1
    
    flip 0->5
    6 3 1 5 2 4
    4 2 5 1 3 6
    
    pass 2 
    1-4 -> position of largest 
    max=5 index=2 
    flip 0 -> 2
    5 2 4 1 3 6
    flip 0 -> 4
    3 1 4 2 5 6
    
    pass 3
    i=3 position of largest 
    max =4 index =2
    flip 0 -> 2
     3 2 1 4 5 6
     
    flip 0 -> 2
    1 2 3 4 5 6 
'''

#Quick Sort
'''
11 88 33 99 44
            P

11 33 88 99 44



Approach 

1.Choose the Pivot as last element

2.Rearrange the array so that 
-- element < pivot leave it 
-- element  > pivot swap
 
3.Repeat the process till all the elements are sorted 

'''

#CODE
'''
def quick(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)
    
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
        
arr=list(map(int,input().split()))
quick(arr,0,len(arr)-1)
print("Sorted array :",arr)
'''
