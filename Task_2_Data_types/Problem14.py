# Set .intersection() Operation

m=int(input())
arr1=set(map(int,input().split()))
n=int(input())
arr2=set(map(int,input().split()))
t=arr1.intersection(arr2)
print(len(t))
