#Enoye Osabuohien
#Intialize
#Functions
def bottles():
        milk=99
        for i in range(98):
            print(str(milk) + " " + "bottles of milk on the wall"+" "+ str(milk)+" "+ "bottles of milk on the wall. Take one down and pass it around")
            milk=milk-1
        print(str(milk)+" "+"bottle of milk on the wall" + " "+str(milk)+" "+ "bottle of milk on the wall. Take one down pass it around")
        print("No more bottles of milk on the wall")
#Main
bottles()
