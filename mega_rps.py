import random

hand = ["rock", "paper", "scissors"]
player_name = " "

def display_welcome_msg():
	print("Hello player, what is your name?")

def player_name():
	player_name = input()
	return player_name
	
def game_instructions(player_name):
	print("Ok {0}, Chose rock, paper, or scissors to start game!".format(player_name))

def player_picks():
	player_picks = input()
	print("You choise {0}".format(player_picks))
	return player_picks

def computer_picks():
	computer_picks = random.choice(hand)
	print("The Computer choise {0}".format(computer_picks))
	return computer_picks

def compare_picks(player_pick, computer_pick):
	if player_pick[0] == "r" or player_pick[0] == "s" or player_pick[0] == "p":
		if player_pick[0] == "r" and computer_pick[0] == "s" or player_pick[0] == "p" and computer_pick[0] == "r" or player_pick[0] == "s" and computer_pick[0] == "p":
			print("player wins")
			return 2
		elif player_pick[0] == computer_pick[0]:
			print("its a tie")
			return 1
		else:
			print("computer wins!")
			return 2
	else:
		print("Choose rock, paper, or scissors you fat dummy!")
		return 1



def run_game(player_name):
	test = 0
	display_welcome_msg()
	player_name = player_name()

	while test != 2:
		game_instructions(player_name)
		test = compare_picks(player_picks(), computer_picks())

run_game(player_name)








 




