balance = 500
purpose = input("Are you here for a withdrawal or balance enquiry? [w/b]")
if(purpose == 'w'):
    pinnumber = input("Enter your pin number here: ")
    withdrawalamount = input(int("How much do you wish to withdraw? "))
    if(withdrawalamount >= 500):
        print("Sorry, you don't have enough money to withdraw that amount.")
    else:
        print(withdrawalamount + " dollars has been withdrawn from your account successfully!")
    
if(purpose == 'b'):
    print("Enter your pin number here: ")
    print(balance)