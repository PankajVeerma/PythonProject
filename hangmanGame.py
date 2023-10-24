import random
word_list = ["ram","shyam","mohan"]
lives =6
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for i in range(len(chosen_word)):
    display += '_' 
print(display)
game_over =False
while(not game_over):
    guess_letter  = input("Guess Letter:").lower()
    print("\r")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter :
            display[position] =guess_letter
    print(display)
    print("\r")        
    if guess_letter not in chosen_word:
        lives -=1    
        if lives == 0:
          game_over=True
          print("You lose")  
    if '_' not in display:      
        game_over= True
        print("YOu Win ")