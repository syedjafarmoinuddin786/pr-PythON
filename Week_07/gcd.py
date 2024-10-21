# WRITE A PROGRAM TO FIND GCD OF TWO NUMBERS
a = int(input())
b = int(input())
if a > b:
	s = b
else:
	s = a
for i in range(1,s+1):
	x1 = a%i 
	x2 = b%i
	if x1 == 0 and x2 == 0:
		v = i
print(v)
