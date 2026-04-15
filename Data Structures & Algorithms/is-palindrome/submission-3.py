class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space=s.replace(" ","")
        #print(no_space)
        actual_str=''.join(char for char in no_space if char.isalnum())
        #print(actual_str)
        reverse_s=actual_str[::-1]
        #print(reverse_s)
        if(actual_str.lower()==reverse_s.lower()):
            return True
        else:
            return False