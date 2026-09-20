class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))
            result += ("#")
            result += (string)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            index = 0
            current_string = ""
            while s[index].isnumeric():
                index += 1
            length = int(s[:index])
            index += 1 # Skip the hash splitter
            current_string = s[index:index+length]
            result.append(current_string) # For list, append:add all, +=: breaks into parts
            s = s[index+length:]
        return result
