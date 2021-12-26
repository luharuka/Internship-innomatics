# Set .difference() Operation

m=int(input())
arr1=set(map(int,input().split()))
n=int(input())
arr2=set(map(int,input().split()))
t=arr1.difference(arr2)
print(len(t))
