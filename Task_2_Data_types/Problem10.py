# Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
arr=list(map(int,input().split()))
n=int(input())
arr2=list(map(int,input().split()))
arr1=set(arr)
arr2=set(arr2)
t=(arr1.difference(arr2)).union(arr2.difference(arr1))
t=list(t)
t.sort()
for i in range(len(t)):
    print(t[i])
