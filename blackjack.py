import time
import random
import msvcrt as m	# for keypress
import os

won = 0
lost = 0

card_chars=['┌','─', '┐','│','░','└','┘','♠', '♥', '♣', '♦']
suits = ['♠', '♥', '♣', '♦']
card_rank = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

cardheight = 9
cardcount = 2
cardwidth = 12

# clubs deck[0-12] diamonds[13-25] hearts[26-38], spades[39-51]


cardpart = ["┌──────────┐", "│░░░░░░░░░░│", "└──────────┘"]


def printCards(hand, yn):
	# position of number and suit on card
	numberheight = 2
	suitheight = int((cardheight-1)/2)

	for rowno in range(cardheight):
		# prints cards in hand in same line
		for counter in range(len(hand)):
			# determines which card part to print
			if rowno == 0:
				print(cardpart[0], end="    ")

			if rowno == cardheight - 1:
				print(cardpart[2], end="    ")
			# prints dealer first card upside down
			if yn is True and counter == 0:
				if cardheight-1> rowno >= 1:
					print(cardpart[1], end="    ")
			else:

				# prints number
				if rowno == numberheight:
					cardn = hand[counter] % 52 % 13 + 1
					print("│░░" + str(card_rank[cardn - 1]), end="")
					if cardn == 10:
						print("░░░░░░│", end="    ")
					else:
						print("░░░░░░░│", end="    ")

				# prints suit

				if rowno == suitheight:
					print("│░░░░" + suits[hand[counter] % 52//13] + "░░░░░│", end="    ")


				else:
					"""if not suit part of card
					and not bottom of card or
					top of card or number part of card
					print middle part of card
					"""
					if rowno != cardheight - 1 and rowno != 0 and rowno != cardwidth/4 - 1:
						print(cardpart[1], end="    ")
				"""
				if rowno == numberheight:
					print(card_value)
				"""
		print("")


def calcScore(playerHand):
	player_points = 0
	ace = False
	for counter in range(len(playerHand)):
		if playerHand[counter] % 52 % 13 + 1 == 1:
			ace = True
		if playerHand[counter] % 52 % 13 + 1 >= 11:
			card_value = 10
		else:
			card_value = playerHand[counter] % 52 % 13 + 1
		player_points += card_value

		"""
		print("card_value is", card_value)
		print("other thing is", playerHand[counter]%52%13 + 1)
		"""
	# changes ace to value of 1 or 11
	if player_points <= 11 and ace is True:
		player_points += 10
	return player_points


def hit(player, deck):
	if player == "player":
		player_hand.append(deck.pop())

	else:
		dealer_hand.append(deck.pop())
	if len(deck) < 4:
		deck = newDeck()


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


def newDeck():
	deck = list(range(52*4))
	random.shuffle(deck)
	return deck


def print_scores():
	print("Your hand: " + str(calcScore(player_hand)) + "        Dealer Hand: " + str(calcScore(dealer_hand)))


def print_stats():
	if lost == 0:
		win_percentage = 1
	else:
		win_percentage = won / (won + lost)
	print("\nYour stats:")
	print("Won: " + str(won) + "    Lost: " + str(lost) + "    Percentage won: " + str(win_percentage * 100) + "%\n")


play_forever = 1
deck = newDeck()

while play_forever:
	dealer_hand = [deck.pop(), deck.pop()]
	player_hand = [deck.pop(), deck.pop()]
	player_points = 0
	clear()
	print("Dealer hand:")
	printCards(dealer_hand, True)
	print("Your hand:")
	printCards(player_hand, False)
	keep_going= "1"

	# get user input
	valid_response = True
	while keep_going == "1" and calcScore(player_hand) < 21:
		if valid_response is not False:
			print("Your Score:", calcScore(player_hand))
		keep_going = input("hit or stand? (h/s, or q to quit) ")

		if keep_going.lower() == "q":
			play_forever = "0"
			break
		elif keep_going == "h":
			hit("player", deck)
			clear()
			print("Your new hand:")
			printCards(player_hand, False)
			valid_response = True
		elif calcScore(player_hand) >= 21:
			break
		elif keep_going == "s":
			break
		else:
			print("Please enter a valid response\n")
			valid_response = True
		keep_going = "1"
	if play_forever == "0":
		break

	if calcScore(player_hand) > 21:
		print("Your (dead) hand: " + str(calcScore(player_hand)))
		print("oof you busted")
		lost += 1
		print_stats()
	else:
		# hit dealer YEET
		while calcScore(dealer_hand) < 17:
			hit("dealer", deck)
			if len(deck) < 1:
				deck = newDeck()
			if calcScore(dealer_hand) == 21:
				break

		print("Dealer's hand:")
		printCards(dealer_hand, False)
		print_scores()

		# see who the dankest mememaker is
		if calcScore(player_hand) <= 21 and calcScore(dealer_hand) > 21:
			print("You win!")
			won += 1
			print_stats()
		elif calcScore(player_hand) > calcScore(dealer_hand) and calcScore(player_hand) <= 21:
			if calcScore(player_hand) == 21:
				print("BLECKJECK BOI")
			else:
				print("you won!")
			won += 1
			print_stats()
		else:
			print("YOU LOST")
			lost += 1
			print_stats()
	print("Press any key to continue...")
	m.getch()
	clear()
	print("")

# after quitting

clear()
print_stats()
