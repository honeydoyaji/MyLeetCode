# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits.reverse()
            i = 0
            while i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                    i += 1
                    if i == len(digits):
                        digits.append(1)
                        break
                    
                else:
                    digits[i] += 1
                    break
                   
            digits.reverse()

        return digits
