class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        print(arr)
        for j in range(0,len(arr)-1):
            if arr[j] == arr[j + 1]:
                return True
        return False