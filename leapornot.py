# TO CHECK WHETHER THE GIVEN YEAR IS LEAP YEAR OR NOT 
y=int(input("Enter the year:"))
if (y%4==0 and y%100!= 0) or (y%400 == 0):
    print("IT IS A LEAP YEAR")
else:
    print("IT IS NOT A LEAP YEAR")
