# Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        binary = bin(num)[2:]
        return (len(binary) + binary.count('1') - 1)