class Solution(object):
    def isPerfectSquare(self, num):
        i = 0
        j = 1
        while i < num:
            i+=j
            if i == num:
                return True
            j+=2
        return False
        
        
        
        
        