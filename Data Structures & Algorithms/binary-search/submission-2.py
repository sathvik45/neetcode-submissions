class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1

        while i<=j:
            idx = int((j+i)/2)
            if target == nums[idx]:
                return idx
            elif target < nums[idx]:
                j = idx-1
            else:
                i = idx + 1
        return -1
