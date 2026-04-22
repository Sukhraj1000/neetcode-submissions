# Define the basic structure of a Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}       # Stores child nodes (next characters)
        self.endOfWord = False   # True if this node marks the end of a valid word

# Define the WordDictionary class which uses the Trie
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()   # Initialize the Trie with a root node

    # Add a word into the Trie
    def addWord(self, word: str) -> None:
        cur = self.root  # Start from the root

        for c in word:  # Loop through each character in the word
            if c not in cur.children:
                cur.children[c] = TrieNode()  # If not found, create a new node
            cur = cur.children[c]  # Move to the next node
        cur.endOfWord = True  # Mark the last character node as end of a word

    # Search a word in the Trie, allowing '.' to match any character
    def search(self, word: str) -> bool:
        
        # Helper function to search recursively using DFS
        def dfs(j, root):
            cur = root  # Start from the current node passed into dfs
            
            for i in range(j, len(word)):  # Loop through the word starting from index j
                c = word[i]
                
                if c == ".":  # '.' can be any letter, so we try all possibilities
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # Recursively check rest of word
                            return True
                    return False  # If none of the paths worked, return False
                
                else:
                    if c not in cur.children:  # If letter not found in children, no match
                        return False
                    cur = cur.children[c]  # Move to the next character node
            
            return cur.endOfWord  # At the end of word, return whether it's a valid word
        
        return dfs(0, self.root)  # Start DFS from index 0 and root node
