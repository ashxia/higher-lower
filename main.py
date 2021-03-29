from game_data import data 
from random import choice
from art import vs
from replit import clear

#pick a random person from data
def choose_player():
  n = choice(data)
  return n


#display the question 
def display(player):
  name = player['name']
  description = player['description']
  country = player['country']

  return f"{name}, a {description}, from {country}"

#return number of followers 
def followers(player):
  return player['follower_count']

#check if answer is right or wrong
def check_answer(A,B, guess):
  if followers(A) > followers(B):
    return guess == "a"
  else:
    return guess =="b"

#start the game
def game():
  A = choose_player()
  B = choose_player()

  game_over = False
  count = 0
  while not game_over:
    a = display(A)
    b = display(B)
    print(f"your score is {count}")

#the game is displayed like this
    print(f"choice A: {a}")
    print(vs)
    print(f"choice B: {b}")
    print(followers(A))
    print(followers(B))

    guess = input("who do you think has more followers A or B?")
    if check_answer(A,B, guess):
      A=B
      count +=1
      B = choose_player()
      clear()
    else:
      print(f"game over you made {count} points")
      game_over = True
   

game()