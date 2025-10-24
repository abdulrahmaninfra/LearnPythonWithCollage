# addition + subtraction - division / mod % floor division // power of **

while True:
    num1= float(input("Enter a First Number: "))
    num2= float(input("Enter a Second Number: "))
    op= input("addition , subtraction , division , mod , floor division , power of , Leave it Blanked and Enter for all: ")

    if op == "addition":
        print("operation of addition equal:", num1+num2)
    elif op == "subtraction":
        print("operation of subtraction equal: ", num1-num2)
    elif op == "division":
        print("operation of division equal: ", num1/num2)
    elif op == "mod":
        print("operation of Mod equal: ", num1%num2)
    elif op =="floor division":
        print("operation of floor division equal: ", num1//num2)
    elif op =="power of":
        print("operation of Power of equal: ", num1**num2)
    elif op == "":
        print("operation of addition equal:", num1+num2)
        print("operation of subtraction equal: ", num1-num2)
        print("operation of division equal: ", num1/num2)
        print("operation of Mod equal: ", num1%num2)
        print("operation of floor division equal: ", num1//num2)
        print("operation of Power of equal: ", num1**num2)

    else:
        print("Invalid  operation, Please check all letters is small")