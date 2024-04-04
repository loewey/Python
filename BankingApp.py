import math 

print("welcome to the online banking system application")



def signup():
    global name 
    global pin 
    global cb 
    name = str(input("please enter the username : "))
    pin = str(input("please enter a 6 digit pin : "))
    if len(pin) == 6:
        pin = pin 
    else:
        print("thats not 6 digits try again")
        newPin = str(input("enter a 6 digit pin : "))
        if(len(newPin) !=6):
            print("the pin must be 6 digits long")
            signup()
        else:
            pin = newPin 
    print("Account created! => Now to log in!")
    login()
    
def forgotPin():
    recoveryPin = str(input("please enter a new 6 digit pin : "))
    if(len(recoveryPin) != 6):
        print("the pin must be 6 digits long : ")
        forgotPin()
    else:
        recoveryPin = pin
        print("the new pin has been set")
        login()

def compoundInterest(p,t,r):
    r = float(r)
    t = float(t)
    p = float(p)
    power = r * t
    e = math.exp(power)
    result = e * p
    return result

def login():
    name1 = str(input("enter your username : "))
    pin1 = str(input("enter your 6 digit pin : "))
    if name1 == name and pin1 == pin:
        print("welcome back to the online banking system")
        print("please pick one of the options below")
        listMenu = ["1-Deposit","2-Withdraw","3-Transfer","4-Check Balance","5-Deposit interest rate","6-Calculate compound interest"]
        for b in listMenu:
            print(b)
        choose = int(input("please enter your choice : "))
        if cb != 0:
            cb = cb 
        else:
         d = 0 
         w  = 0
         cb = 0 
        if choose == 1:
            d = int(input("enter the amount you with to deposit : "))
            cb = d 
            newBalance = cb + d
            print("your current balance is £" + str(newBalance))
        elif choose == 2:
            w = int(input("enter the amount you wish to withdraw : "))
            if w > cb:
                print("insufficient funds")
                login()
            else:
                cb = cb-w
                print("Transaction complete current balance is £" + str(cb))
        elif choose == 3:
            dest = str(input("enter the 8 digit account number : "))
            if len(dest) == 8:
                amount = int(input("enter the amount you wish to transfer : "))
                if amount > cb:
                    print("insufficient funds")
                else:
                    cb = cb- amount
                    print("The transaction has been completed of amount £"+str(amount) + " to the account of number "+str(dest))
            else:
                print("transaction denied as invalid account number")
                login()
        elif choose == 4:
            print("your current balance is : £"+str(newBalance))
        elif choose == 5:
            d = float(input("enter a diposit"))
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print ("your current diposit rate is : " + str(rate)+"%")
        elif choose == 6:
            listOption = ["1-Calculate your compound interest based on your CB","2-Calculate your compound interest based on your deposit input"]
            for n in listOption:
                print(n)
            choiceInterest = int(input("Enter your choice below : "))
            if choiceInterest == 1:
                timing = float(input("how many years were you going to keep the money : "))
                if cb > 50000:
                    ratex = 3/100
                elif cb > 30000:
                    ratex  = 2/100
                else: 
                    ratex = 1.5/100
                compoundInterest(cb,timing,ratex)
            elif choiceInterest == 2:
                inputAmount = float(input("please enter the amount : "))
                timing1 = float(input("enter the amount of time you wish to keep the money : "))
                if inputAmount > 50000:
                    ratex = 3/100
                elif inputAmount > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                compoundInterest(inputAmount,timing1,ratex)
            else:
                print("error has occured due to invalid choice")
        else:
            print("error has occured due to invalid choice")
            login()
        exit()
        
    else:
        print("Either of your username or password is incorrect, have you previously created an account with us?")
        choice = ["1-yes","2-no"]
        for i in choice:
            print(i)
        inp = int(input("Enter your choice below : "))
        if inp == 1 :
            list2  = ["1-you with to attempt at logging in again","2- you have forgot your pin"]
            for e in list2:
                print(e)
            inp2 = int(input("Enter your choice below : "))
            if inp2 == 1:
                login()
            elif inp2 == 2:
                print("forget pin, please reset the pin")
                forgotPin()
            else:
                print("option is not available")
        elif inp == 2:
            print("please create your account")
            signup()
        else:
            print("an error has occured invalid option")

       
def mainMenu():
    optionnone = int(input("Choose 1 to sign up and 2 to log in : "))
    if optionnone == 1 :
        signup()
    elif optionnone == 2:
        login()
    else:
        print("error has occured that was not an option")

def exit():
    answer = str(input("Do you wish to still conduct the transaction? Yes or No : "))
    if answer == "Yes":
        login()
    elif answer == "No":
        print("Thank you for banking with us today")
    else:
        print("An error has occured due to invalid option")
        mainMenu()
    
mainMenu()