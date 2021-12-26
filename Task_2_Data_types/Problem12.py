

# Set .discard(), .remove() & .pop()


m=int(input())
s=set(map(int,input().split()))
n=int(input())
for i in range(n):
    arr=input().strip().split()
    if arr[0]=="remove":
        s.remove(int(arr[1]))
    if arr[0]=="pop":
        s.pop()
    if arr[0]=="discard":
        s.discard(int(arr[1]))
print(sum(s))



