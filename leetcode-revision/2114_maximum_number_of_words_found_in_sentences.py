class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
       
        max_count=0

        for sentence in sentences:
            count= len(sentence.split())   ## split() separates sentence into words and len() counts them

            max_count = max(count,max_count)

        return max_count