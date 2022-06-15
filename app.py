# https://learn.nucamp.co/mod/assign/view.php?id=4109&action=view

# I am importing the account file from the banking_pkg file.
from banking_pkg import account
# I can now use everything in the account file. Functions and all!
# import a whole file and all of its functions and variables.
# from selects which functions and variables you want to use from a file.
# if I want to use the import method I have to put filenameiampulling.
# import method make a directory list to it. for each function or variable or something you want to call from the file. banking_pkg.account.deposit


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
balance = 0
name = input("Enter name to register:")
pin = input("Enter PIN:")
print(name, "has been registered with a starting balance of: $", balance)

while True:
    print("LOGIN")
    # the input function will show enter name and the user will input their name.
    name_to_validate = input("Enter name: ")
    # if they input something different than what is registered it will stop the code here.
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("invalid credentials!")
    # if name_to_validate and pin
while True:
    atm_menu(name)  # see code above
    option = input("Choose an Option:")
    if option == "1":  # make sure that this is a string because thats what the input function generates. If statements must have a colon.
        # access the account files functions using the file name with period and the function.
        account.show_balance(balance)
    elif option == "2":
        # updating balance after deposit. see account.py. it stores that calculation in return.
        balance = account.deposit(balance)
        account.show_balance(balance)
        # tough way to do it. comment this out once the point is learned.
        # print("Your new balance is:", balance)
        # account.show_balance(balance) #using the function from account show balance. this is a function that shows the balance on its own.
        # You need that calculations result to be used to redefine the balance variable. so make the balance variable be reassigned to the new variable.
    elif option == "3":  # This needs
        balance = account.withdraw(balance)
        account.show_balance(balance)
        # print("Your new balance is:", balance) print is the tough way to do it. comment this out once the point is learned.
    # these need to be in strings because the input function the User is using is a string.
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid Selection")

        # understanding import vs from
        # input rules as a string and converting
        # f string formatting
