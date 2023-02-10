import random
correct= random.randint(1,9)
while 1:
    guess_num=int(input('Enter your guess:'))
    if(guess_num==correct):
        print('Well Gussed')
    else:
        print('Try Again')
    
