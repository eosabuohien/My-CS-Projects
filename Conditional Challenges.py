# Condtional statements

#Initalize
#Functions
#Challenge 1
# 18 years of age or older
# U.S citzen
def vote_check():
    #Collect your input
    #Process the data using conditonals
    age = int(input("Please enter your age: "))
    citizen = ("Are you a U.S citizen(yes or no):")
    if age > 18 and citizen == "yes" :
        print ("You are eligible to vote")
    else:
        print("You are not eligible to vote")

#Challenge 2
# a= int b=int c=int
#Function prints the largest number out of a,b, and c
def max_num(a,b,c):
    #No input needed
    #Figure out which is the largest, conditional statements
    if a > b and a > c :
        print("A is the largest number, the value of a is: " + str(a))
def max_num2(a,b,c):
    if b > a and a > c :
        print("B is the largest number, the value of b is: " + str(b))
def max_num3(a,b,c):
    if c > a and a > b:
        print("C is the largest number, the value of c is: " + str(c))

def score_to_grade(score):
    #No input needed/score is input
    #Conditionals go here
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score >= 50:
        print ("F")
    elif score>= 40:
        print("F")
    elif score>= 30:
        print ("F")
    elif score >= 20:
        print("F")
    elif score>= 10:
        print("F")
    elif score >= 0:
        print("F")

#Main
vote_check()
max_num(15,5,10)
max_num2(5,15,3)
max_num3(5,3,15)
score_to_grade(90)
score_to_grade(80)
score_to_grade(70)
score_to_grade(60)
score_to_grade(50)
score_to_grade(40)
score_to_grade(30)
score_to_grade(20)
score_to_grade(10)
score_to_grade(0)
