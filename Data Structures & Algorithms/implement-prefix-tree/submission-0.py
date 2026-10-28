class TrieNode:
    def __init__(self):
        self.children = {} # A trie may need to branch to 26 diff chars (alphabet), so we track with "char: [addr of next node]""
        self.endword = False # also keep track of end of work

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children: # Check current node has node for letter
                curr.children[char] = TrieNode() # Create new node
            curr = curr.children[char] # Move pointer to new node
        curr.endword = True # Remember to mark end of word when done

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children: # Check current node has node for letter
                return False # If it doesn't exist return False 😎😎😎
            curr = curr.children[char] # Move pointer to new node if found
        return curr.endword # Remember if it reaches end of word its True, so just return True again!

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True # Same as search, but default to True since it made it to the end of the prefix