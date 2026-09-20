class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for g in range(len(nums)):
            compare = nums[g]
            for h in range(g,len(nums)):
                another = nums[h]
                if compare + another ==target:
                    for r in range(len(nums)):
                        if nums[r] == another:
                            array = []
                            array.append(g)
                            array.append(r)
                            return array
        