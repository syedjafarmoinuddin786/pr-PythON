''' DONE BY ME
def su(a,b):
	print("Sum of the Values ",(a+b))
def sub(a,b):
	print("Difference of the two numbers",(a-b))
def mul(a,b):
	print("Multiplication of the numbers",(a*b))
def div(a,b):
	print("Divison of the numbers",(a/b))					
print("ENTER THE VALUES:")
a = int(input())
b = int(input())
su(a,b)
sub(a,b)
mul(a,b)
div(a,b) '''

''' ACTUAL SOLUTION '''
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
print("Addition :",add(a,b))
print("Subtraction :",sub(a,b))
print("Multiplication :",mul(a,b))
print("Divison :",div(a,b))
	
