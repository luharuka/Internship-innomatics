# Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a=list(dict.fromkeys(arr))
    t=max(a)
    a.remove(t)
    print(max(a))
    
