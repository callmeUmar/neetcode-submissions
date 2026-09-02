class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1
        res = []
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.append(l + 1)
                res.append(r + 1)
                break
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        return res









        # Numbers order - non-decreasing -> 1 , 2 ,3 ,4 ,5
        #
        # We have to return the indicies [index 1] [index 2] -> so they add up to target number
        #
        # Index 1 and Index 2 cannot be equal
        #
        # Basically , Example , target = 3 , the list is [1,2,3,4] the index of 1st and 2nd values 
        # 3. It's because the value is 3 not sum of indexes.
        #






