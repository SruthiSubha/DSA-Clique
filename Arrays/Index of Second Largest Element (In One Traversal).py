array=[]
nums=int(input())
for i in range(nums):
    array.append(int(input()))
maximum=max(array)
second=0
for i in range(0,nums):
    if array[i]!=maximum:
        second=max(second,array[i])
print(second)
