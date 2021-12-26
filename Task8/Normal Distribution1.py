# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cd(mean, std, x):
    return  0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


mean, std = list(map(float, input().split(' ')))
a = float(input().strip())
b,c = list(map(float, input().split(' ')))
    
print("%.3f" % cd(mean, std, a))
print("%.3f" % (cd(mean, std, c) - cd(mean, std, b)))
