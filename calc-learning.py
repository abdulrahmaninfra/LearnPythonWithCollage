first= float(input("Enter your first number: "))
second= float(input("Enter your second Number: "))

op= input("Enter your operation + ,- ,* ,/ ,** ,%:")

if op== "+":
    result= first+second
    print("Result of operation is:", result)
elif op== "-":
    result= first-second
    print("Result of operation is:", result)
elif op== "*":
    result= first*second
    print("Result of operation is:", result)
elif op== "**":
    result= first**second
    print("Result of operation is:", result)
elif op== "%":
    result= first%second
    print("Result of operation is:", result)
elif op== "/":
    if second == 0:
        print("Error, you can divide by zero ")
    else:
        result = first/second
        print("Result of operation is:", result)

else:
    print("Error, Please select your operation")

