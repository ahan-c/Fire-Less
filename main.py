import time
print("Welcome to the air pollution game!")
print("\nBefore moving on we're going to show a website which we've made with a lot of effort!")
print("Please take time to have a look at it.\n")
print("\nOpening website...")
time.sleep(2.25)
import web
i = input("Continue(yes/no)?")

if i.lower() == "yes":
    print("\nOK! Nice choice let's continue.")
    print("Let's see how much you know about the environment.\n")
    ans1 = input("Is air pollution good or bad?")
    opt1 = ["bad","good"]
    if ans1.lower() == opt1[0]:
        print("\nNice choice!!")
    elif ans1.lower() == opt1[1]:
        print("\nHmmm, Not really the choice...")

    ans2 = input("\n\nDo you want to light crackers on diwali(yes/no):")
    opt2 = ["no","yes"]
    if ans2.lower() == opt2[0]:
        print("\nHmm, you really do care about the environment.")
    elif ans2.lower() == opt2[1]:
        print("\nEnvironment destroyer!")
    
    #ans3 = input("\n\n")
    
elif i.lower() == "no":
    print("\nPlease visit again if you have time.")
    print("Hope you had a nice time!")