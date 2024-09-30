#PRACTICING SETS,TUPLES,STRINGS syntax.

#TUPLES

#repetition
""" t=(1,2,5,'ab','bc','cd')
print(t*3) """
#index
""" t=(12,34,45,56,67,78)
print(t[0])
print(t[2])
print(t[4]) """
#membership operator
""" t = ('ab','bc','cd','de')
print('abc' in t)
print('ab' in t) """ 
# iteration
""" for i in (1,2,3):
	print(i) """
#slicing
""" t = (12,23,34,45,56,67,78,89)
print(t[::2])
print(t[::1])
print(t[-1::2])
print(t[:-1])
print(t[2:-1])
print(t[:4])
print(t[3:]) """
# TUPLE METHODS
#indexing and length and count()
""" t = (12,23,34,23,45,56,67,78,89,45,56)
print(t.index(56))
print(len(t))
print(t.count(23)) """
#copy
""" t1 = ('ab','bc','cd','de')
t2 = ('ef','fg','gh','hi')
t3 = t1+t2
print(t3) """
#Zip
"""t1 = (12,23,34,45,56,67,78,89)
t2 = (90,10,20,30,40,50,60,70)
t3 = tuple(zip(t1,t2))
print(t3) """
