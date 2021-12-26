# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import erf,sqrt

mx = int(input())
n = int(input())
mean = int(input()) 
std = int(input()) 
std = std/sqrt(n)  
y = mx/n 
cdf = lambda x: 0.5 * (1 + erf((x-mean)/(std*sqrt(2))))

print(round(cdf(y),4))