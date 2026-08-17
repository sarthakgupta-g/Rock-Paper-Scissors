import random

i=0
computer_points=0
player_points=0

while(i<3):
  computer=random.choice(["rock","paper", "scissors"])
  player=input("enter move")
  

  if(computer=="rock"):
    if(player=="rock"):
        print("tie")
    elif(player=="paper"):
        print("player wins round!")
        player_points+=1
    elif(player=="scissors"):
        print("computer wins round!")
        computer_points+=1
  elif(computer=="scissors"):
    if(player=="rock"):
        print("player wins round!")
        player_points+=1
    elif(player=="paper"):
        print("computer wins round!")
        computer_points+=1
    elif(player=="scissors"):
        print("tie")
  elif(computer=="paper"):
    if(player=="rock"):
        print("computer wins round!")
        computer_points+=1
    elif(player=="paper"):
        print("tie")
    elif(player=="scissors"):
        print("player wins round!")
        player_points+=1
  i+=1
  
if(player_points>computer_points):
    print("Player wins!")
elif(player_points<computer_points):
    print("Computer wins!")  
else:
  print("tie game")
