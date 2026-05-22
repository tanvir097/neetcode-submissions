class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = "".join(sorted(list(s)))
        word2 = "".join(sorted(list(t)))

        if word1 == word2:
            return True
        else:
            return False