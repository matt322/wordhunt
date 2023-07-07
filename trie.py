import pickle

class TrieNode():
    def __init__(self, val) -> None:
        self.children = {}
        self.val = val
    
    def __hash__(self) -> int:
        return hash(self.val)
    
    def __eq__(self, __value: object) -> bool:
        return self.val == __value\
        
    def __str__(self) -> str:
        return ','.join(self.children)

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode("$")

    def add(self, word):
        node = self.root
        for char in word+'$':
            if not char in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]

if __name__ == '__main__':
    t = Trie()
    with open('words.txt') as words:
        for word in words.readlines():
            t.add(word[:-1])

    pickle.dump(t, open('trie.pickle', 'wb'))