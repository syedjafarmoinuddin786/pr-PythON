# sum & average of the list
l = []
n = int(input("ENTER THE RANGE OF THE LIST:"))
for i in range(n):
    lis = int(input())
    l.append(lis)
s = sum(l)
avg = s//n
print(s)
print(avg)
