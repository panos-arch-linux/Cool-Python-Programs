from colorama import Fore

print(Fore.RED + "Exam Grade Calculator")

a = input(Fore.WHITE + "Name of the Exam:")
maxScore = int(input("Max possible score:"))
score = float(input("Your score:"))

percentage1 = score / maxScore * 100
percentage = round(percentage1, 1)

if percentage  >=90:
    print ("Your got", percentage, "%, which is an A+")
    exit()
    
elif percentage  >= 80 and percentage <=89 :
    print ("Your got", percentage, "%, which is an A")
    exit()              
elif percentage  >= 70 and percentage <=79 :
    print ("Your got", percentage, "%, which is a B")
    exit()
elif percentage  >= 60 and percentage <=69 :
    print ("Your got", percentage, "%, which is a C")
    exit()
elif percentage  >= 50 and percentage <=59 :
    print ("Your got", percentage, "%, which is a D")
    exit()
elif percentage  <50:
    print ("Your got", percentage, "%, which is a U")
    exit()
else:
    exit()
