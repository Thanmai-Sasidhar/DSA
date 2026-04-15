#Insertion sort 

'''
Approach

1.Start from 2nd value assuming 1st index value as sorted \
  
  for i --> 1 to n-1   

2.pick the current element with key

key=arr[i]

3.compare with previous elements

while j>=0 and arr[j]>key

4.shift all the largetst elements to the right

    arr[j+1]=arr[j]
 
5.insert the key in position 

6.sorted till sorted       
'''

#CODE
'''
arr=list(map(int,input().split()))
n=len(arr)

for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("Sorted Elements :",arr)
'''

#DRY RUN    
'''
Input: 5 3 4 1

Initial Array:
[5, 3, 4, 1]





Pass 1 (i = 1)
key = 3
j = 0
arr[0] = 5 > 3 → shift
[5, 5, 4, 1]
Insert key at position 0
[3, 5, 4, 1]






Pass 2 (i = 2)
key = 4
j = 1
arr[1] = 5 > 4 → shift
[3, 5, 5, 1]
j = 0
arr[0] = 3 < 4 → stop
Insert key at position 1
[3, 4, 5, 1]






Pass 3 (i = 3)
key = 1
j = 2
arr[2] = 5 > 1 → shift
[3, 4, 5, 5]
j = 1
arr[1] = 4 > 1 → shift
[3, 4, 4, 5]
j = 0
arr[0] = 3 > 1 → shift
[3, 3, 4, 5]
j = -1
Insert key at position 0
[1, 3, 4, 5]

Final Sorted Array:
[1, 3, 4, 5]


'''
        
#Merge Sort

'''
               15 5 24 8 3 16 10 20

        15 5 24 8             3 16 10 20                      

    15 5       24 8         3 16       10 20
  
  15    5    24     8      3    16   10     20  


'''
#Algo
'''
1.If array has 1 element then sorted 

2.If not divide array into 2 halves recursively 

3.After getting independent values sort recursively both halves

4.merge the 2 sorted arrays 

'''

#Program
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    # remaining elements
    res.extend(left[i:])
    res.extend(right[j:])
    
    return res

# Input
arr = list(map(int, input().split()))
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
'''























