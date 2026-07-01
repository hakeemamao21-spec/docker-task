def fact_iter(n):
 """assumes n an int >= 0"""
 answer = 1
 while n > 1:answer *= n
 n -= 1
 return answer
