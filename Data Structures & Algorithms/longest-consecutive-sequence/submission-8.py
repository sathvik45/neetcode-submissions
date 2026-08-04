class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp =list(set(nums))
        print(temp)
        nums1=sorted(temp,reverse=False)
        print(nums1)
        i,j=0,1
        c=0
        while i < len(nums1) and j < len(nums1):
            temp=0
            while j<len(nums1) and nums1[i] +1 == nums1[j]:
                temp+=1
                i+=1
                j+=1
            c=max(c,temp)
            i+=1
            j+=1
        return c+1
        # while i+1 < len(nums):
        #     temp=0
        #     while nums[i]+1 == nums[i]:
        #         temp+=1
        #         i+=1
        #     c=max(temp,c)
        #     i+=1
        # return c




