# Lists


if __name__ == '__main__':
    N = int(input())
    l=list()
    for i in range(N):
        arr=input().split()
        if arr[0]=="insert":
            l.insert(int(arr[1]),int(arr[2]))
        elif arr[0]=="print":
            print(l)
        elif arr[0]=="remove":
            l.remove(int(arr[1]))
        elif arr[0]=="append":
            l.append(int(arr[1]))
        elif arr[0]=="sort":
            l.sort()
        elif arr[0]=="pop":
             l.pop()
        elif arr[0]=="reverse":
            l.reverse() 

