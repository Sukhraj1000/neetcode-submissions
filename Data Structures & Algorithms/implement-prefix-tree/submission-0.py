# Each TrieNode represents a single character
class TrieNode:
    def __init__(self):
        self.children = {}       # A dictionary to store child nodes (next characters)
        self.endOfWord = False   # Flag to indicate if this node marks the end of a full word

# This is our main Trie (Prefix Tree) structure
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()   # Start with an empty root node

    # Function to add a word to the Trie
    def insert(self, word: str) -> None:
        cur = self.root  # Start from the root

        for c in word:  # Loop through each character in the word
            if c not in cur.children:
                cur.children[c] = TrieNode()  # If the character doesn't exist, create a new node
            cur = cur.children[c]  # Move to the child node
        cur.endOfWord = True  # After the word is fully inserted, mark the last character as end of word

    # Function to check if a word exists in the Trie
    def search(self, word: str) -> bool:
        cur = self.root  # Start from the root

        for c in word:
            if c not in cur.children:
                return False  # If character not found, word doesn't exist
            cur = cur.children[c]  # Move to the next character
        return cur.endOfWord  # Only return True if this path ends a word

    # Function to check if any word in the Trie starts with the given prefix
    def startsWith(self, prefix: str) -> bool:
        cur = self.root  # Start from the root
        
        for c in prefix:
            if c not in cur.children:
                return False  # If character not found, no word with that prefix
            cur = cur.children[c]
        return True  # We found all characters in the prefix, so return True