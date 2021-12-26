# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

def combination(num, x):
    return factorial(num) / (factorial(x) * factorial(num-x))

def b(x, n, p):
    return combination(n, x) * (p**x) * ((1-p)**(n-x))


p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))