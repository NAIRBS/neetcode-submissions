class TrieNode:
    def __init__(self):
        self.children = {}
        self.endword = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endword = True

    def search(self, word: str) -> bool:
        def dfs(index, curr):
            for i in range(index, len(word)):
                char = word[i]
                if char == ".": # If it's a wildcard, try all children of the current node
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else: # Normal character lookup
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.endword
        return dfs(0, self.root)