# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf
mean, std = 70, 10
cdf = lambda x: .5 + .5 * erf((x - mean)/2**.5/std)

print(round((1 - cdf(80)) * 100, 2))
print(round((1 - cdf(60)) * 100, 2))
print(round(cdf(60) * 100, 2))