# Set Mutations

m=int(input())
arr1=set(map(int,input().split()))
n=int(input())
for i in range(n):
    arr=list(input().split())
    arr2=set(map(int,input().split()))
    if arr[0]=="update":
        arr1.update(arr2)
    if arr[0]=="intersection_update":
        arr1.intersection_update(arr2)
    if arr[0]=="difference_update":
        arr1.difference_update(arr2)
    if arr[0]=="symmetric_difference_update":
        arr1.symmetric_difference_update(arr2)
print(sum(arr1))
