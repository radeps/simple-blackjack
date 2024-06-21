

from random import randint
from random import shuffle

cards = {
	1 : 'A',
	2 : '2',
	3 : '3',
	4 : '4',
	5 : '5',
	6 : '6',
	7 : '7',
	8 : '8',
	9 : '9',
	10 : '10',
	11 : 'J',
	12 : 'Q',
	13 : 'K'
}

suits = [0, 1, 2, 3]

deck = [(v, s) for v in cards.keys() for s in suits]
shuffle(deck)

pull_card = lambda d : d.pop(randint(0,len(d)-1))

net_chips = 0

show_hand = lambda h : [cards[c[0]] for c in h]
#sum_hand = lambda h : sum([min([10, c[0]]) for c in h])

def sum_hand(hand):
	aceless_sum = sum([min([c[0],10]) for c in hand if c[0] != 1])
	# At most one ace can be 11
	aces = [c[0] for c in hand if c[0] == 1]
	total_sum = aceless_sum
	if aces:
		total_sum += (11 * len(aces))
		while aces and total_sum > 21:
			aces.pop()
			total_sum -= 10
	return total_sum



dealer_cards = []
player_cards = []

while True:

	input("Press enter to continue.")
	deck += dealer_cards
	deck += player_cards
	shuffle(deck)

	print("===============================")
	print("Playing in active shuffle mode.")
	print(f"You have {net_chips} chips.")
	print("Your bet is 1 chip.") 

	player_bet = 1

	dealer_cards = [pull_card(deck), pull_card(deck)]
	
	player_cards = [pull_card(deck), pull_card(deck)]

	print(f"The dealer has {cards[dealer_cards[0][0]]}. ({min(dealer_cards[0][0], 10)})")

	choice = "h"

	if True:
		
		print(f"Your cards = {show_hand(player_cards)}. ({sum_hand(player_cards)})")
		
		print("H to hit, S to stay.")
	
		while True:

			choice = input(">>> ")

			if choice not in ["h", "s"]:
				print("Um, ok...")
				continue

			if choice == "s":
				break

			hit_card = pull_card(deck)
			player_cards.append(hit_card)
			print(f"Pulled {cards[hit_card[0]]}. ({sum_hand(player_cards)})")
			if sum_hand(player_cards) > 21:
				break

		if sum_hand(player_cards) > 21:
			print("You have gone bust!")
			print("You lose 1 chip.")
			net_chips -= 1
			continue

		input(f"Dealer reveals his cards: {show_hand(dealer_cards)}. ({sum_hand(dealer_cards)})")
		
		while sum_hand(dealer_cards) <= 16 or (sum_hand(player_cards) > sum_hand(dealer_cards) and sum_hand(player_cards) <= 21):
			hit_card = pull_card(deck)
			dealer_cards.append(hit_card)
			input(f"Dealer pulled {cards[hit_card[0]]}. ({sum_hand(dealer_cards)})")


		if sum_hand(dealer_cards) > 21:
			print("Dealer has gone bust!")
			if sum_hand(player_cards) <= 21:
				print("You win 1 chip.")
				net_chips += 1
				continue
		else:
			print(f"Dealer stands on {sum_hand(dealer_cards)}.")

		if sum_hand(player_cards) > 21:
			print("You lose 1 chip.")
			net_chips -= 1
			continue
		
		if sum_hand(player_cards) == sum_hand(dealer_cards):
			print("You break even.")
			continue
	
		if sum_hand(player_cards) > sum_hand(dealer_cards):
			print("You win 1 chip.")
			net_chips += 1
			continue
		
		else:
			print("You lose 1 chip.")
			net_chips -= 1
			continue

		

		
















