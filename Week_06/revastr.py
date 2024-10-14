# REVERSE OF A STRING WITH SLICE OPERATOR 
print('ENTER THE STRING:')
s = (input())
print(s[::-1])

# WITHOUT SLICE OPERATOR
print('ENTER THE STRING :')
s = input()
r = ''
for i in s:
	r = i + r
print(r)	
