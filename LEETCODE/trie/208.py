# 208. Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False # True if node represent the end of the word
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): # if not present, insert word into trie
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children: # if not current character is not present
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True # last node as leaf "끝"이라고 알려줌.

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
            
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)