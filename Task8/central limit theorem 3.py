# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
n = int(input())
u = int(input())
r = int(input())
p = float(input())
z = float(input())
me = ( z * r )/ math.sqrt(n)
A = u - me
B = u + me
print(round(A, 2))
print(round(B, 2))