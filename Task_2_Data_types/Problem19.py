
# Check Subset

if __name__=="__main__":
    for _ in range(int(input())):
        n, a = input(), set(input().split())
        m, b = input(), set(input().split())
        print(all([i in b for i in a])) 