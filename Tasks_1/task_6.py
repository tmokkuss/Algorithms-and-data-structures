import random

word_list = ["кошка", "собака", "хомяк", "компьютер", "нейронка", "дерево", "лес"]

secret_word = random.choice(word_list)

hidden_word = "_" * len(secret_word)

max_attempts = 6

guessed_letters = []


def display_game_state():
    print("Угадываемое слово:", hidden_word)
    print("Угаданные буквы:", guessed_letters)
    print("Осталось попыток:", max_attempts)


def handler():
    while True:
        player_input = input("Введите букву: ").lower()
        if len(player_input) != 1:
            print("Пожалуйста, введите одну букву.")
        elif not player_input.isalpha():
            print("Пожалуйста, введите букву.")
        elif player_input in guessed_letters:
            print("Вы уже угадывали эту букву. Попробуйте другую.")
        else:
            return player_input


while max_attempts > 0 and hidden_word != secret_word:
    display_game_state()
    player_input = handler()
    guessed_letters.append(player_input)
    if player_input in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == player_input:
                hidden_word = hidden_word[:i] + player_input + hidden_word[i + 1:]
    else:
        max_attempts -= 1

if max_attempts == 0:
    print("Вы проиграли. Загаданное слово было:", secret_word)
else:
    print("Вы выиграли! Загаданное слово было:", secret_word)
