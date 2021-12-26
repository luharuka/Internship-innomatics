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

m,n = list(map(float, input().split(" ")))
par = m / n
print(round(sum([b(i, 6, par / (1 + par)) for i in range(3, 7)]), 3))