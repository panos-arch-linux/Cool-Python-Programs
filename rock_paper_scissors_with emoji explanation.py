#print(emoji.demojize('📃'))==> this command converts an emoji into code so you can then include it into your python code
import emoji
from getpass import getpass as input # hides what players have typed in
print(emoji.emojize("Epic Rock Paper Scissors Battle :rock: :page_with_curl: :scissors:"))
print()
print("Select your move (R, P or S)")
print()
player1 = input("Player 1>")
player2 = input("Player 2>")


if player1 == "R" and player2 == "S":
    print("Player1's Rock smashes Player2's Scissors!")
    exit()
elif player2 == "R" and player1 == "S":
    print("Player2's Rock smashes Player1's Scissors!")  

elif player1 == "R" and player2 =="P":
    print("Player2's Paper devours Player1's Rock...")
    exit()
elif player1 == "P" and player2 =="R":
    print("Player1's Paper devours Player2's Rock...")
    exit()

elif player1 == "R" and player2 == "R":
    print("This is a breathtaking draw")
    exit()
    
elif player1 == "S" and player2 == "P":
    print("Player1's Scissors rip Player2's Paper")
    exit()
elif player2 == "S" and player1 == "P":
    print("Player2's Scissors rip Player1's Paper")    
    exit()
    
elif player1 == "S" and player2 == "S":
    print("This is a breathtaking draw")
    exit()
elif player1 == "P" and player2 == "P":
    print("This is a breathtaking draw")
    exit()
  



