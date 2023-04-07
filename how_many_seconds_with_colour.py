from colorama import Fore, Back, Style
print(Fore.RED + 'How many seconds are in a Year?')

hour = 60 * 60
day = hour * 24
total = day * 365.25

question = input(Fore.YELLOW + "Is this a leap year?")
if question == "no" or question == "No" or question =="NO":
    print(Fore.GREEN + "")
    print("It's", total, "seconds")
    exit()
else:
    leap = 366 * 24 * 60 * 60
    print("It's",leap, "seconds")
    exit()
    
