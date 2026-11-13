from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        # Pre-compute generic wildcard patterns
        all_combo_dict = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        # Bidirectional BFS structures
        begin_set = {beginWord}
        end_set = {endWord}
        visited = {beginWord, endWord}
        
        level = 1
        
        while begin_set and end_set:
            # Always expand the smaller set to optimize the search space
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                
            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in all_combo_dict[pattern]:
                        if neighbor in end_set:
                            return level + 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_set.add(neighbor)
            
            begin_set = next_set
            level += 1
            
        return 0