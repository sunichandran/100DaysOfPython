import random

# create a random list of words
word_list = ["aardvark", "baboon", "camel"]

# choose a ramdom word
chosen_word = random.choice(word_list)

#Testing code
print(f'Psst..the word is {chosen_word}. ')

# display "_" for all the letters in the chosen_word
display = []
word_length = len(chosen_word)
end_of_game = False


for _ in range(word_length):
  display += "_"

# ask the user an input/guess the letter
guess = input("Guess a letter").lower()

# check the guess with the chosen_word. if the guessed letter matches the letter in the chosen_word, print the letter in that position
while not end_of_game:
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  print(display)
  if "_" not in display:
    end_of_game = True
    print("You win.")
    




