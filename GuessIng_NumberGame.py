import random# import(import krne ke liye) ek modul hai ,,,aur random (give range me random variable lene ke liye) bhi ek modul hai
random_num = random.randint(0,1000)
number_of_guess = 0
print('You have only 10 guess,between 0_1000')
while(number_of_guess<10):
    guess_number = int(input('Guess the number'))
    if guess_number<random_num:
     print('increase number\n')
    elif guess_number>random_num:
       print('Decrease number\n')
    else:
       
       print('you win\n')

       print()
       print(number_of_guess,' number of guess you took till now\n')
       break
    number_of_guess = number_of_guess +1
       

print(10-number_of_guess,'number of guess you have left')
number_of_guess = number_of_guess +1
if(number_of_guess>10):
    print('Game over')

