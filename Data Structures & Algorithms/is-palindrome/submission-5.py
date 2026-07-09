class Solution:
    def isPalindrome(self, s: str) -> bool:

        str = ("".join(char for char in s if char.isalnum())).lower()
        ptr1 = 0
        ptr2 = len(str)-1

        while ((ptr1 != ptr2) and (ptr1<ptr2)):
            if (str[ptr1] == str[ptr2]):
                ptr1 += 1
                ptr2 -= 1
            else:
                return False
        return True   
        