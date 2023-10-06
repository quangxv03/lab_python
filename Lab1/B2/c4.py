"""4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không"""

import math
def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x
def isFibonacci(n):
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n = int(input("Nhập n: "))
check = isFibonacci(n)
if check== True:
	print(f"{n} là số fibonacci")
else:
	print(f"{n} không là số fibonacci")