import random

word_list = ["pickle","home","catostrophic","alphabet"]
display = [""]
chosen_word = random.choice(word_list)
lives = 6
for letter in chosen_word:
    display += "_"
print(chosen_word)
# print(display)



end_of_game = False
while not end_of_game:
    guess = input("Guess a letter?").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("you lose")

if "_" not in display:
    end_of_game = True
    print("you win")