#Enoye Osabuohien
#11/18/24
#Init
#Functions
def addition(num1,num2):
    answer=num1 + num2
    print(answer)
def subtraction(num1,num2):
    answer=num1 - num2
    print(answer)

def multiplication(num1, num2):
    answer= num1 * num2
    print(answer)
def division(num1,num2):
    answer= num1 / num2


print("Welcome to Simple Calculator!")
def simplecalculator():
    while True:
        print ("Please choose an operation")

        print("""1.Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Quit""")
        menu=int(input("1-5:"))
        if menu == 1:
            num1=int(input("Please enter the first number:"))
            num2=int(input("Please enter the second number:"))
            addition(num1,num2)
        if menu== 2:
            num1=int(input("Please enter the first number:"))
            num2=int(input("Please enter the second number:"))
            subtraction(num1,num2)
        if menu== 3:
            num1=int(input("Please enter the first number:"))
            num2=int(input("Please enter the second number:"))
            multiplication(num1,num2)
        if menu== 4:
            num1=int(input("Please enter the first number:"))
            num2=int(input("Please enter the second number:"))
            division(num1,num2)
        if menu==5:
            print("Quit")
            break
#Main


simplecalculator()
