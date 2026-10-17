class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        char = list(s)

        for i in range(0, len(char), 2*k):
            char[i:i+k] =  reversed(char[i:i+k])

        return "".join(char)