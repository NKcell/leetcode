class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        return [i+extraCandies>=maxNum for i in candies]