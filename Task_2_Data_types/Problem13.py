# Set .union() Operation

m=int(input())
arr=set(map(int,input().split()))
n=int(input())
arr2=set(map(int,input().split()))
t=arr.union(arr2)
print(len(t))