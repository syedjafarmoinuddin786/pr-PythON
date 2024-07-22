print("f to c" " or " "c to f")
x=str(input("WHAT CONVERSION DO YOU WANT: "))
if x == ("f to c"):
    # TEMPERATURE CONVERSION Fahrenheit to Celsius
    f= float(input("ENTER THE TEMPERATURE in fahrenheit:"))
    c=(f-32)*5/9
    print("TEMPERATURE IN CELSIUS:") 
    print(c)
elif x == ("c to f"):
    #TEMPERATURE CONVERSION Celsius to Fahrenheit
    c=float(input("ENTER THE TEMPERATURE in celsius:"))
    f=(c*9/5)+32
    print("TEMPERATURE IN FAHRENHEIT:")
    print(f)
else:
    print("INVALID INPUT")
      
   
