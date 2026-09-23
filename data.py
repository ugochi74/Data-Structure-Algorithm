class TrieNode:
    def __init__(self):
        # Maps a character to the next TrieNode
        self.children = {}
        # Stores the frequency of the word if it ends here (0 means not a word)
        self.frequency = 0

class AutocompleteSystem:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, weight: int = 1):
        """Inserts a word into the Trie and updates its search frequency."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.frequency += weight  # Mark end of word and add weight
