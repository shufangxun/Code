class Solution:
    def verifySequenceOfBST(self, sequence):
        if  not sequence:
            return True 
            
        start = 0
        while sequence:
            while sequence[start] < sequence[-1]:
                start += 1
            while sequence[start] > sequence[-1]:
                start += 1
            
            if start < len(sequence) - 1 :
                return False

            sequence.pop()
            start = 0
        
        return True
    
        


        