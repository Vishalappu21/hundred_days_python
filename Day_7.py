import random

string= ["vishal",'prasanna','anbu']
Lives = 8
string_ran = random.choice(string)
placeholder = ""
word_len = len(string_ran)
for i in range(word_len):
    placeholder += "_"
print(placeholder)
game_over = False
correct_letter = []
while not game_over:
    user = input("Enter the Letter: ").lower()
    display = ""
    for letter in string_ran:
        if letter == user:
            display += letter
            correct_letter.append(user)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if user not in string_ran:
        Lives -= 1
        if Lives == 0:
            game_over = True
            print("You Lose")

    if "_" not in display:
        game_over = True
        print(f"You Win, you find the Word.and the word is {string_ran}")
        break