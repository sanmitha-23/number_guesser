from random import randint
from art import logo

EASY_TURNS=10
HARD_TURNS=5

def validate(number,guess,turns):
  if guess>number:
    print("Too high")
    return turns-1
  elif guess<number:
    print("Too low")
    return turns-1
  else:
    print(f"You have got the answer right!! The number was {number}")
    
def set_difficulty():
  choice = input("Choose a difficulty. Type 'easy' or 'hard'\n--->")
  if choice=='easy':
    return EASY_TURNS
  elif choice=='hard':
    return HARD_TURNS

def game():
  print(logo)
  print("Welcome to the number guessing game!!")
  print("I'm thinking of a number between 1 and 100")
  number=randint(1,100)
  print(number)

  turns = set_difficulty()

  guess=0

  while guess!=number:
    print(f"You have {turns} attempts left")

    guess=int(input("Enter your guess: "))

    turns = validate(number,guess,turns)
    
    if turns==0:
      print("You have run out of attempts")
      return
    elif guess!=number:
      print("Guess again")


game()
