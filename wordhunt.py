import pickle
from trie import Trie, TrieNode

t = pickle.load(open('trie.pickle', 'rb'))

grid = []
a = ['first', 'second', 'third', 'fourth']
for i in range(4):
    inp = input("{} row: ".format(a[i])).upper()
    while len(inp) != 4 or not inp.isalpha():
        print('enter four letters')
        inp = input("{} row: ".format(a[i])).upper()
    grid.append(list(inp))

answers = []

moves = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def search(row, col):
    res = []
    node = t.root
    def dfs(row, col, node, string, seen = set()):
        if '$' in node.children:
            res.append(string)
        for move in moves:
            r = row+move[0]
            c = col+move[1]
            if 0 > r or r > 3 or 0 > c or c > 3 or (r, c) in seen or grid[r][c] not in node.children:
                continue
            newstring = string+grid[r][c]
            newset = set(seen)
            newset.add((r,c))
            dfs(r, c, node.children[newstring[-1]], newstring, newset)

    dfs(row, col, node, '')
    return res

for row in range(4):
    for col in range(4):
        answers.extend(search(row, col))

answers = list(dict.fromkeys(answers))
answers.sort(key = lambda x: len(x))
for i in answers:
    print(i)

input()
