# TO PRIMT THE WORDS HAVING EVEN LENGTH
print("ENTER THE STRING :")
s = input()
count = 0
s1 = s.split(" ")
for i in s1:
 	if(len(i)%2 == 0):
 	   print(i)
 	   
