class Solution:
    def fib(self, n: int) -> int:
        m=0
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            m=self.fib(n-1)+self.fib(n-2)
            return m
        

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.