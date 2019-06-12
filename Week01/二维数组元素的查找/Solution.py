class Solution(object):
    def searchArray(self, array, target):
        """
        :type array: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if array == [] or array[0] == []:
            return False
            
        i = 0 
        j = len(array[0]) - 1
        
        while(i < len(array) and j >= 0):
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j -= 1
            else:
                i += 1
        
        return False

  
