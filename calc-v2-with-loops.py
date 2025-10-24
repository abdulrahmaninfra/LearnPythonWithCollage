while True:
    op= input("Enter Operation (+,-,/,^,//) or q or quit: ")

    if op == "q":
        break

    num1= float(input("Enter the Number: "))
    num2=float(input("Enter the Number: "))

    if op == "+":
        print("Result: ",num1+num2)
    elif op == "-":
        print("Result: ",num1-num2)
    elif op == "/":
        print("Result: ",num1/num2)
    elif op == "^":
        print("Result: ",num1^num2)
    elif op == "//":
        print("Result: ",num1//num2)
    else:
        print("Try Again")
