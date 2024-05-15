class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i in range(len(nums)):
            compliment = target-nums[i]
            if compliment in hash_map:
                # If you find the compliment in the map then just send the cordinates on which you are sitting
                return [hash_map[compliment], i]
            # Still solution is not found just input the element in the hash map with corresponding location in the list
            hash_map[nums[i]] = i


a = Solution()
print(a.twoSum([2, 7, 11, 15], 9))
