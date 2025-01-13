#Enoye Osabuohien
#10/18/2024
#Name Generator
#Which Marvel Superhero or Villain are You?
print ("Which Marvel Superhero/Villain are You?")
print("Answer the questions to find out what you are")
ans = input("Superhero(s) or Villain(v)?")
if ans=="s":
    ans=input("male(m) or female(f)")
    if ans=="m":
        ans= input("immortality(i) or superstrength(s)")
        if ans=="i":
            print("Your superhero is Thor")
        else:
            print("Your superhero is Captain America")
    if ans=="f":
        ans=input("witchcraft(w) or assassin(a)")
        if ans=="w":
            print("Your superhero is Scarlet Witch")
        else:
            print("Your superhero is Black Widow")
if ans=="v":
    ans=input("God(g) or Domination(d)")
    if ans=="g":
        ans=input("illusion(il) or trickery(t)")
        if ans=="il":
            print ("Your villain is Hela")
        else:
            print("Your villain is Loki")
    if ans=="d":
        ans= input("warlord(wa) or Robot(r)")
        if ans=="wa":
            print("Your villain is Thanos")
        else:
            print("Your villain is Ultron")

