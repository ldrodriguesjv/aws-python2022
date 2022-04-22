"""
Your module description
"""
import random

print("Bem-vindo ao Adivinhe o Número!")
print("As regras são simples. Vou pensar em um número e você tentará adivinhar.")
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Escolha um numero entre 1 e 10: ")

    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))