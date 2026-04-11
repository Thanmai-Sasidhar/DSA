#Array Implementations

'''
1.Second Largest

2.Rotation of Array

3.traverse/reverse array 

4.move all zeroes to end

5.Roatate left with key positions

6.kadens algorithm

'''

#Rotate an array right by 1
'''
arr=list(map(int,input().split()))
last=arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last
print(arr)
'''
'''
#DRY RUN
arr=[1,2,3,4,5]
last=arr[-1]-->5
i=4
for 4 in range(5-1,0,-1):
    arr[4]=arr[3] #1 2 3 4 4
    
i=3
for 3 in range(5-1,0,-1):
    arr[3]=arr[2] #1 2 3 3 4

i=2
for 2 in range(5-1,0,-1):
    arr[2]=arr[1] #1 2 2 3 4

i=1
for 1 in range(5-1,0,-1):
    arr[1]=arr[0] #1 1 2 3 4
    
arr[0]=last # 5 1 2 3 4
'''    
#Move all zeroes to an end 
'''
arr=list(map(int,input().split()))
zero=0
for i in range(len(arr)):
    if arr[i]!=0:  # IF WE PLACE == it will be left shift
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print("After moving Zeroes:",arr)        
'''

'''
DRY RUN

1.arr=[0,1,0,3,2]
zero=0

2.arr[i]=1
as 1!=0
swap 0-1 -> 1-0
zero=1

3.
arr[i]=2
0
zero=1
skip

4.arr[i]=3
3!=0
swap 0-3 --> 3-0

5.i==4
arr[i]!=0
2!=0
swap 0-2 --> 2-0

'''
#Reverse elements for sorted array
'''
arr=list(map(int,input().split()))
for i in range(len(arr)//2):
    arr[i],arr[(len(arr)-1)-i]=arr[(len(arr)-1)-i],arr[i]
print(arr)   
''' 
#Reverse elements for array (sorted and unsorted)
'''
arr=list(map(int,input().split()))
start=0
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
print(arr)    
'''

#Subarray sum
'''
arr=list(map(int,input().split()))        
maxsum=0
curr=arr[0]
for i in range(1,len(arr)):
    curr=max(maxsum,curr+arr[i])
    maxsum=max(maxsum,curr)
print("Max sum is :",maxsum)    
'''
'''
arr=[1,2,3,-1,-2,-3,0,4]
sum1=0
for i in arr:
    if i>0:
        sum1+=i
print(sum1)        
'''
DRY RUN

'''








