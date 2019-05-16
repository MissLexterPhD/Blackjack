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
                    print(cardValue)
                """
        print("")


def calcScore(playerHand):
    playerPoints = 0
    ace = False
    for counter in range(len(playerHand)):
        if playerHand[counter]%52%13 + 1 == 1:
            ace = True
        if playerHand[counter]%52%13 + 1 >= 11:
            cardValue = 10
        else:
            cardValue = playerHand[counter]%52%13 + 1
        playerPoints += cardValue
        
        """
        print("cardValue is", cardValue)
        print("other thing is", playerHand[counter]%52%13 + 1)
        """
    # changes ace to value of 1 or 11
    if playerPoints <= 11 and ace is True:
        playerPoints += 10
    return playerPoints


def hit(player):
    if player == "player":
        player_hand.append(deck.pop())
        
    else:
        dealer_hand.append(deck.pop())


def clear():
    os.system("cls")


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


playforever = 1
deck = newDeck()
while playforever:
	if len(deck) < 4:
		deck = newDeck()
	dealer_hand = [deck.pop(), deck.pop()]
	player_hand = [deck.pop(), deck.pop()]
	playerpoints = 0
	clear()
	print("Dealer hand:")
	printCards(dealer_hand, True)
	print("Your hand:")
	printCards(player_hand, False)
	keepgoing= "1"
	# hit player
	validresponse = True
	while keepgoing == "1" and calcScore(player_hand) < 21:
		if validresponse is not False:
			print("Your Score:", calcScore(player_hand))
		keepgoing = input("hit or stand? (h/s, or q to quit) ")
		if keepgoing.lower() != "h" and keepgoing.lower() != "s" and keepgoing.lower() != "q":
			print("Please enter a valid response\n")
			validresponse = True
		elif keepgoing.lower() == "q":
			playforever = "0"
			break
		elif keepgoing == "h":
			hit("player")
			clear()
			print("Your new hand:")
			printCards(player_hand, False)
			validresponse = True
		elif calcScore(player_hand) >= 21:
			break
		elif keepgoing == "s":
			break
		keepgoing = "1"
	if playforever == "0":
		break
	if calcScore(player_hand) > 21:
		print("Your (dead) hand: " + str(calcScore(player_hand)))
		print("oof you busted")
		lost+=1
		print_stats()
	else:
		# hit dealer
		while calcScore(dealer_hand) <= 17:
			hit("dealer")
			if calcScore(dealer_hand) == 21:
				break
		print("Dealer's hand:")
		printCards(dealer_hand, False)
		print_scores()
		if calcScore(player_hand) <= 21 and calcScore(dealer_hand) > 21:
			print("You win!")
			won+=1
			print_stats()
		elif calcScore(player_hand) > calcScore(dealer_hand) and calcScore(player_hand) <= 21:
			if calcScore(player_hand) == 21:
				print("BLECKJECK BOI")
			else:
				print("you won!")
			won+=1
			print_stats()
		else:
			print("YOU LOST")
			lost+=1
			print_stats()
	print("Press any key to continue...")
	m.getch()
	clear()
	# time.sleep(3)
	#  [ 7, 21], 8, 9
	print("")

# after quitting

clear()
print_stats()
