class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subsets = []
            for subset in result: # Look at every subset created so far
                new_subset = subset + [num] # Just add the new element!
                new_subsets.append(new_subset) # Add that into the list of new subsets!
            result.extend(new_subsets) # Add new subsets into results
        #result += [subset + [num] for subset in result] # One liner magic
        return result