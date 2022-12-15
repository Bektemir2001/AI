m, n = map(int, input().split())

s = 10**(m-1)
k = 10**m
num1 = 0
num2 = 0

while s < k:
	tmp = 0
	l = s 
	while l > 0:
		tmp += l%10
		l //= 10
	if tmp == n:
		num1 = s 
		break
	s += 1 
k -= 1 

while k > 0:
	tmp = 0
	l = k 
	while l > 0:
		tmp += l%10
		l //= 10
	if tmp == n:
		num2 = k 
		break
	k += 1 
print(num1, num2)