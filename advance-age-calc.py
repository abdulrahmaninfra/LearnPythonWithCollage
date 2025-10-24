from datetime import datetime

day= datetime.now().day
month= datetime.now().month
year= datetime.now().year

# ud is user birthday , md is User birth Month , yd is User birth Year 

ud=float(input("Enter your birthday: "))
md=float(input("Enter your birth month: "))
yd=float(input("Enter your birth year: "))

ld= day - ud
lm= month - md
ly= year - yd


print(ld)
print(lm)
print(ly)



