from getpass import getpass as input
print("\033[33mEPIC 🪨 📜 ✂ BATTLE\033[0m")
print(" ")
print("Select your move (R for Rock, P for Paper, S for Scissors) ")
player1 = input("Player 1: ")
player2 = input("Player 2: ")
print(" ")
if player1 == player2:
    print("It's a draw!")
elif player1 == "R" and player2 == "S":
    print("Player 1 wins!")
elif player1 == "P" and player2 == "R":
    print("Player 1 wins!")
elif player1 == "S" and player2 == "P":
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
