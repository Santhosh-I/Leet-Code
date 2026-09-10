class Solution:
    def fib(self, n: int) -> int:

        a , b = 0 , 1
        fibo = []

        for i in range(30):
            fibo.append(a)
            a , b = b , a + b
        
        if n <= 1:
            return n
        else:
            return fibo[n - 1] + fibo[n - 2]
            

        