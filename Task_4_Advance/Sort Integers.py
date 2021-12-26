# Sort Integers by The Number of 1 Bits
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda xr: (bin(xr).count("1"), xr))