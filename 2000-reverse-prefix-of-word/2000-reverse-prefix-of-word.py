class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.index(ch) if word.find(ch) != -1 else -1
        return word[:idx+1][::-1] + word[idx+1:] if idx != -1 else word