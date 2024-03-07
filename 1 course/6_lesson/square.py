import random

def square(n, m ,t):
	nm = n * m
	l = -1
	r = min(n, m) // 2 + 1
	while r - l > 1:
		mid = (l + r) // 2
		s = (n - mid * 2)*(m - mid * 2)
		if nm - s <= t:
			l = mid
		else:
			r = mid

	return l if l > -1 else 0    
n, m, t = [int(input()) for i in range(3)]
print(square(n, m ,t))
