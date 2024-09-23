#INTERCHANGE THE FIRST AND LAST ELEMENT OF THE LIST
l = []
n = int(input("ENTER THE RANGE OF THE LIST:"))
for i in range(n):
  lis = int(input())
  l.append(lis)
temp = l[0]
l[0] = l[n-1]
l[n-1] = temp
print(l)
