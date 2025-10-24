# GPA Calcultor
import webbrowser
score= float(input("Enter your Score: "))

if score >= 90:
    grade= "A"
    gpa= 4.0
    print("Congrats!!!, Your GPA is" , gpa , "and Grade is", grade)

elif score >= 80:
    grade= "B"
    gpa= 3.0
    print("Congrats!!!, Your GPA is" , gpa , "and Grade is", grade)
    

elif score >= 70:
    grade= "C"
    gpa= 2.0
    print("Next time will be better , Your GPA is" , gpa , "and Grade is", grade)

elif score >= 60:
    grade= "D"
    gpa= 1.0
    print("you can do better , Your GPA is" , gpa , "and Grade is", grade)

elif score <= 60:
    grade= "F"
    gpa= 0.9 
    print("Sorry :( , Your GPA is" , gpa , "and Grade is", grade)

