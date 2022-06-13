'''

Given a 2D board and a list of words from the dictionary, find all words in the board.

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
'''

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


def findWords(board, dictionary):
    t = Trie()
    node = t.root
    for word in dictionary:
        t.insert(word)

    for i in range(len(board)):
        for j in range(len(board)):
            word = ""
            DFS(board, i, j, node, word)

def DFS(board, i, j, node, word):


    if i < 0 or i > len(board) - 1 or j < 0 or j > len(board) - 1:
        return

    if not node:
        return

    letter = board[i][j]

    if node.isWord == True:
        print(word)
        node.isWord = False

    word += letter

    DFS(board, i + 1, j, node.children.get(letter), word)
    DFS(board, i - 1, j, node.children.get(letter), word)
    DFS(board, i, j-1, node.children.get(letter), word)
    DFS(board, i, j+1, node.children.get(letter), word)

    DFS(board, i + 1, j-1, node.children.get(letter), word)
    DFS(board, i + 1, j+1, node.children.get(letter), word)
    DFS(board, i - 1, j+1, node.children.get(letter), word)
    DFS(board, i - 1, j-1, node.children.get(letter), word)

    return

dictionary = ['pie', 'apple', 'pine', 'pineapple']

board = [['p', 'e', 'a'],
         ['i', 'n', 'p'],
         ['e', 'l', 'p']]

findWords(board,dictionary)
