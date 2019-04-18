class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            digits[-1] = 0
            carry = 1
        else:
            digits[-1] += 1
            carry = 0
        for i in range(len(digits) - 2, -1, -1):
            m = carry
            carry = (digits[i] + carry) // 10
            digits[i] = (digits[i] + m) % 10
        if carry == 1:
            digits.insert(0, 1)
        return digits
