import time
print("Welcome to Fire Less!")
print("\nBefore moving on we're going to show a website which I've made with a lot of effort!")
print("Please take time to have a look at it.\n")
print("\nOpening website...")
points = 0
time.sleep(2.2)
import web
i = input("Continue(yes/no)?")

if i.lower() == "yes":
    print("\nOK! Nice choice let's continue.")
    print("Let's see how much you know about the environment.\n")
    print("For each nice choice you make, you get 1 point.\n")
    ans1 = input("Is air pollution good or bad?(good/bad):")
    opt1 = ["bad","good"]
    if ans1.lower() == opt1[0]:
        print("\nNice choice!!")
        points+=1
    elif ans1.lower() == opt1[1]:
        print("\nHmmm, Not really the choice...")

    ans2 = input("\n\nDo you want to light crackers on diwali?(yes/no):")
    opt2 = ["no","yes"]
    if ans2.lower() == opt2[0]:
        print("\nHmm, you really do care about the environment.")
        points+=1
    elif ans2.lower() == opt2[1]:
        print("\nEnvironment destroyer!")
    
    ans3 = input("\n\nWould you be willing to use green crackers instead of the normal ones?(yes/no):")
    opt3 = ["yes","no"]
    if ans3.lower() == opt3[0]:
        print("\nNice, I respect you from now on.")
        points+=1
    elif ans3.lower() == opt3[1]:
        print("\nYou've just gained some disrespect from me.")
    
    ans4 = input("\n\nWould you be willing to tell people to stop the usage of dangerous firecrackers?(yes/no):")
    opt4 = ["yes","no"]
    if ans4.lower() == opt4[0]:
        print("\nThanks a lot")
        points+=1
    if ans4.lower() == opt4[1]:
        print("\nNo thanks")
    
    ans5 = input("\n\nWould you be willing to tell people about this program?(yes/no):")
    opt5 = ["yes","no"]
    if ans5.lower() == opt5[0]:
        print("\nThanks again")
        points+=1
    if ans5.lower() == opt5[1]:
        print("\nNo fun then")

    time.sleep(0.2)
    print("\nYour quiz ends here.\n")
    print("You scored"+" "+str(points)+"/5"+" points.")
    print("I hope you had a nice time!")

elif i.lower() == "no":
    print("\nPlease visit again if you have time.")