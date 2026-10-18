class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(s)
        left = 0
        right = len(s)-1

        while left < right:
            if not chars[left].isalnum():
                left+=1
            elif not chars[right].isalnum():
                right-=1
            else:
                if chars[left].lower() != chars[right].lower():
                    return False

                left += 1
                right -= 1
        
        return True