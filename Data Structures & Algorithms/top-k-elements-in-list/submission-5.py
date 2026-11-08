class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        output = []
        freq = Counter(nums)
        for number, count in freq.items():
            bucket[count].append(number)
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                output.append(num)
            if len(output) == k:
                return output
        return output