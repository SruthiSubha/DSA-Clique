#Index of Second Largest Element (In One Traversal) in python

#1. Brute force Approach
array=[]                        # An Array is initialized
nums=int(input())               # nums is the size of an array
for i in range(nums):           # traversing from 0 to nums-1 
    array.append(int(input()))  # Appending the elements to the list array
array.sort()                    # sorting the elements in ascending order
for i in range(nums-2,-1,-1):   # itersating from reverse order from last second element to first element
    if array[i]!=array[nums-1]: # Checking the condition if second element is equal to last element if yes, then print the required element and break the loop
        print(array[i])
        break
        
#2. Simpler Approach
array=[]                            # An Array is initialized
nums=int(input())                   # nums is the size of an array
for i in range(nums):               # traversing from 0 to nums-1
    array.append(int(input()))      # Appending the elements to the list array
maximum=max(array)                  # Finding the maximum element in list and storing the element in maximum variable
second=0                            
for i in range(0,nums):             # iterating through the list of elements
    if array[i]!=maximum:           # checking whether element is not equal to current element if yes then taking maximum out of it
        second=max(second,array[i])
print(second)                         


