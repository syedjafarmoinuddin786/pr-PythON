# wrtie a program to define a function which returns multiple values
# let us take the example of the rectangle
print("ENTER THE VALUES OF LENGTH AND BREADTH:") 
l = int(input())
b = int(input())
def area_and_perimeter_rect(l,b):
	area = l*b
	perimeter = 2*(l+b)
	return area,perimeter 
print("AREA and PERIMETER OF THE RECATNGLE",area_and_perimeter_rect(l,b))
 
