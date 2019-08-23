#
# Give the user the following options. Once the option that is selected is completed keep asking them until they hit 4 to quit:
#
# ```
# Hello, please choose one of following options:
# 1) Check balance
# 2) Add money to account
# 3) Withdraw money from account
# 4) Quit
# What will you like to do?
# ```
# '''
# The user menue and input. Four options to direct the user, Check Balance, Deposit, Withdraw, and quit
#
# '''
userInput = ""
while userInput != "4":
    print(userInput)
    print(f"1.) Check Balance.\n"
          f"2.) Deposit into account.\n"
          f"3.) Withdraw from account.\n"
          f"4.) Quit.")
    # '''
    #     # Was having a hard time placing the input above the choices with the menu. Placed here till end. Will continue to debug if there is more time.
    # '''
    userInput = input("Hello, user. Choose one of the following options above.- ")

#print is for formmating space

    print("         ")

# '''
# Adding the if conditionals fro the 3 options. Because the quit option is true statement it does not need one.
# '''
#     '''
#     # This is the first option. This only checks what is in the account
#
#     '''
    currentBalance = 0
    if currentBalance == 0:
        option1quit = ""

        if userInput == "1":
            print(f"User has ${currentBalance} in their account")


        if userInput == "2":
            print(f'User has ${currentBalance} in their account')
            moneyCount = int(input("How much would you like to deposit?- "))
            newBalance = moneyCount+currentBalance

            if newBalance != 0:
                print(f'User now has ${newBalance} in their account.')

        withdrawlAmnt = 0
        if userInput == "3":
            print(f'User currently has ${newBalance}')
            withdrawlAmnt = int(input("How much would you like to withdraw?- "))
            if withdrawlAmnt != 0:
                print(f'User now has ${newBalance-withdrawlAmnt} in their account.')

            if withdrawlAmnt > newBalance:
                print("Insufficient funds.")


print("Have a good day!")