class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

def minExtraChar(s, dictionary):
    trie = Trie(dictionary).root
    dp = { len(s): 0 }

    def dfs(i):
        if i in dp:
            return dp[i]
        res = 1 + dfs(i + 1)
        curr = trie
        for j in range(i, len(s)):
            if s[j] not in curr.children:
                break
            curr = curr.children[s[j]]
            if curr.word:
                res = min(res, dfs(j + 1))
        dp[i] = res
        return res
    return dfs(0)