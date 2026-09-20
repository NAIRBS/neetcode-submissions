class Solution: # More optimallerer 21st Sep Revision

    def encode(self, strs: List[str]) -> str:
        # One-line f-string combined with join() allocates memory exactly once.
        return "".join(f"{len(string)}#{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        current_index = 0  # Global pointer prevents expensive string copying/slicing
        while current_index < len(s): # Find where the number ends and '#' starts
            current_word_index = current_index
            while s[current_word_index] != '#':
                current_word_index += 1
            length = int(s[current_index:current_word_index]) # Extract length safely
            # Slice the exact word and append it intact
            word = s[current_word_index + 1 : current_word_index + 1 + length]
            result.append(word)
            # Advance pointer past the processed word
            current_index = current_word_index + 1 + length
        return result