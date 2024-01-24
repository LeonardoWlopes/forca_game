import os
from random import randint

def stop_game():
    print("Game Over!")

def draw_hangman(lives, word, guessed_letters):
    head = "O" if lives < 5 else " "
    body = "|" if lives < 4 else " "
    arms = "/|\\" if lives < 3 else " "
    legs = "/ \\" if lives < 2 else " "

    print("______")
    print("|    |")
    print("|    " + head)
    print("|   " + arms)
    print("|    " + body)
    print("|   " + legs)

    placeholder = ""
    for letter in word:
        if letter in guessed_letters:
            placeholder += letter + " "
        elif letter == " ":
            placeholder += "  "
        else:
            placeholder += "_ "
    print(placeholder[:-1])  # Removendo o espaço extra no final

def await_input():
    input("Pressione enter para continuar...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verify_guesses(lista, string):
    string = string.lower()
    return all(char in lista for char in string)

def play_hangman():
    file_path = "words.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        words = [line.strip().lower() for line in file.readlines()]

    word = words[randint(0, len(words) - 1)]

    guessed_letters = []
    lives = 5 if len(word) < 10 else 5
    game_won = False  # Adicionado para rastrear se o jogo foi ganho

    while lives > 0:
        clear_screen()

        print(f"Vidas Restantes: {'❤' * lives}")
        print(f"Tamanho da palavra: {len(word)}")
        draw_hangman(lives, word, guessed_letters)

        guess = input("Digite uma letra: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Digite apenas uma letra!")
            await_input()
            continue

        if guess in guessed_letters:
            print("Você já tentou essa letra!")
            await_input()
            continue

        if guess not in word:
            lives -= 1
            print("Letra errada!")
            await_input()
        else:
            guessed_letters.append(guess)

        if set(char for char in word if char != ' ') == set(guessed_letters):
            clear_screen()
            draw_hangman(lives, word, guessed_letters)
            input("Você ganhou!")
            game_won = True  # O jogo foi ganho
            break  # Sair do loop

    if not game_won:  # Se o jogo não foi ganho, exibir "Game Over!"
        stop_game()

if __name__ == "__main__":
    play_hangman()
