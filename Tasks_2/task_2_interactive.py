import tkinter as tk
from itertools import product


def create_app():
    app = tk.Tk()
    app.title("Колода игральных карт")

    card_label = tk.Label(app, text="", font=("Arial", 14))
    card_label.pack(pady=10)

    removed_suit = input("Введите масть, которая будет выброшена (пик, треф, бубен, червей): ")

    suits = ['пик', 'треф', 'бубен', 'червей']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

    suits.remove(removed_suit)

    cards = product(ranks, suits)

    def update_card():
        try:
            rank, suit = next(cards)
            card_label.config(text=f"{rank} {suit}")
        except StopIteration:
            card_label.config(text="Карты закончились")

    next_button = tk.Button(app, text="Следующая карта", command=update_card)
    next_button.pack(pady=10)

    update_card()

    app.mainloop()


create_app()
