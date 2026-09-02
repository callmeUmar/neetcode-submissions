class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        seen = {}
        p = 0

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        while p < k:
            key = max(seen, key=seen.get)
            maxes.append(key)
            seen[key] = 0
            p += 1

        return maxes