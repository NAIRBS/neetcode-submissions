class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Naive n ^ 2 solution
        # result = []
        # found = 0
        # for i in range(len(temperatures)):
        #     found = 0
        #     for j in range(len(temperatures)):
        #         if temperatures[j] > temperatures[i] and j > i:
        #             result.append(j-i)
        #             found = 1
        #             break
        #     if found == 0: result.append(0)
        # return result

        # Turns out we need to use a monotonic stack? (decreasing)
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result
