# Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=="__main__":
    for _ in range(int(input())):
        n, a = input(), set(input().split())
        m, b = input(), set(input().split())
        print(all([i in b for i in a])) 
