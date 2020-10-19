import math


def payment(pricipal, months):
    return int(math.ceil(pricipal/months))


def last(pricipal, months):
    return principal - (months - 1)*payment(principal, months)


def month(principal, monthly):
    a = principal//monthly
    mod = principal%monthly
    if mod == 0:
        return a
    else:
        return a+1


def plural(principal, monthly):
    a = principal/monthly
    if a == 1:
        return 'month'
    else:
        return 'months'


principal = int(input("Enter the loan principal:"))
print("What do you want to calculate?")
print('type "m" - for number of monthly payments,')
print('type "p" - for the monthly payment:')
choice = input()
if choice == 'm':
    monthly = int(input("Enter the monthly payment:"))
    print("It will take", month(principal, monthly), plural(principal, monthly), "to repay the loan")

elif choice == 'p':
    months = int(input("Enter the number of months:"))
    if principal%months == 0:
        print("Your monthly payment =", payment(principal, months))
    else:
        print("Your monthly payment =", payment(principal, months), "and the last payment =", last(principal, months))
