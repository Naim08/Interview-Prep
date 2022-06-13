# Python program for insert and search
# operation in a Trie

from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord

    def getChildren(self, letter):
        return self.root.children.get(letter)
