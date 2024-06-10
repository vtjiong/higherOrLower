import art
import game_data as gd
import random
from replit import clear

score=0
def compare(a,b):
  if a >b:
    return 'A'
  else:
    return 'B'
score=0
previous=random.choice(gd.data)
while True:
  print(art.logo)
  if (score!=0):
    print(f"You're right, Your current score is {score}")
  a=previous
  b=random.choice(gd.data)
  print(f"Compare A: {previous['name']}, {previous['description']}, from {previous['country']}")
  print(art.vs)
  print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")
  user_answer=input("Who has more followers? Type 'A' or 'B': ").upper()
  answer=compare(a['follower_count'],b['follower_count'])
  if user_answer==answer:
    score+=1
    if answer == 'A':
      previous = previous
    else:
      previous = b
    clear()
  else:
    break
clear()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")   