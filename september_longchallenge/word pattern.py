class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words=str.split()
        if len(pattern)!=len(words):
            return False
        char={}#{'a':'dog','b':'cat'}
        word={}#{'dog':'a','cat':'b'}
        for c,w in zip(pattern,words):
            if c not in char:
                if w not in word:
                    char[c]=w
                    word[w]=c
                else:
                    return False
            else:
                if char[c]!=w:
                    return False
        return True
            
