# A Trie (pronounced "try"), also known as a prefix tree, is a specialized tree-based 
# data structure used to efficiently store and retrieve keys in a dataset of strings. 
# Instead of storing an entire word in a single node, each node in a Trie represents a 
# single character. Words that share the same starting characters share the same 
# ancestral path down the tree, making it incredibly powerful for prefix-based operations.

# Core Architecture & Node Design
# A standard Trie consists of a root node that remains empty or holds a null value. 
# Every other node contains two main components:

# 1. Children References: A collection mapping characters to child nodes. 
# This can be implemented as a fixed-size array (e.g., size 26 for English lowercase 
# letters) or a dynamic hash map/dictionary.

# 2. Boolean Flag (isEndOfWord): A marker designating whether the path from the root 
# to this specific node constitutes a complete, valid word.



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True



## Example Usage

trie = Trie()

trie.insert('apple')
trie.insert('app')

print(trie.search('apple'))
print(trie.search('app'))
print(trie.search('appl'))
print(trie.starts_with('ap'))