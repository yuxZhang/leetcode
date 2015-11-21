__author__ = 'yuxiangZhang'
class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        temp = self.root
        for k in word:
            if k not in temp.children:
                temp.children[k] = TrieNode()
            temp = temp.children[k]
        temp.isWord = True

    def search(self, word):
        return self.findWord(self.root, word)

    def findWord(self, node, word):
        for k in range(len(word)):
            if word[k] != '.':
                if word[k] in node.children:
                    node = node.children[word[k]]
                else:
                    return False
            else:
                for child in node.children:
                    if self.findWord(node.children[child], word[k+1:]):
                        return True
                return False
        return node.isWord


x = WordDictionary()
x.addWord("a")
x.addWord("ab")
print(x.search("a."))
