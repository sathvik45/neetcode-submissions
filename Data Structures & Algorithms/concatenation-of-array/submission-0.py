class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = nums
        n.extend(nums)
        return n