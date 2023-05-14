from itertools import product

removed_suit = input("Введите масть, которая будет выброшена (пик, треф, бубен, червей): ")

suits = ['пик', 'треф', 'бубен', 'червей']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

suits.remove(removed_suit)

cards = product(ranks, suits)

for card in cards:
    rank, suit = card
    print(rank, suit)