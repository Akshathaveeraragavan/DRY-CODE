#MONTY HALL SIMULATION PROBLEM
'''Monty hall’s problem comes from a famous movie where three doors are used to help you win a car. How? Each door hides something behind it–a car and two goats.
Any door can have the car while the remaining two have goats. The probability to find a car is 1⁄3. Now, if you select Door 1 and the host opens Door 3 to find a goat,
your chances just become 2⁄3.'''
#LETS ASSUME : DOOR 1 & 3 HAS GOATS AND DOOR 2 HAS THE CAR  
doors=['1','2','3']
print('WELCOME TO PLAY THE FAMOUS GAME : MONTY HALL SIMULATION PROBLEM')
player=int(input('Which door you choose?'))
if player==1:
    print('You chose door 1')
    print('DOOR 3 OPENED')
    player_choice=input('DO YOU WANT TO SWITCH?\nY/N')
    if player_choice=='Y' or player_choice=='y':
        choice2=int(input('SWITCH TO WHICH DOOR?\n1/2?'))
        if choice2==1:
            print('YOU WON THE CAR')
        else:
            print('You chose door 2 ')
            print('DOOR 1 OPENED')
            player_choice=input('DO YOU WANT TO SWITCH?\nY/N')
            if player_choice=='Y' or player_choice=='y':
                print('YOU LOSE!!!')
            else:
                print('YOU WON THE CAR  !!!')
    else:
        print('YOU LOSE!!!')

elif player==2:
    print('You chose door 2')
    print('DOOR 1 OPENED')
    player_choice=input('DO YOU WANT TO SWITCH?\nY/N')
    if player_choice=='Y' or player_choice=='y':
        choice2=int(input('SWITCH TO WHICH DOOR?\n2/3?'))
        if choice2==2:
            print('YOU WON THE CAR !!!')
        else:
            print('You chose door 3')
            player_choice=input('DO YOU WANT TO SWITCH?\nY/N')
            if player_choice=='Y' or player_choice=='y':
                print('YOU WON THE CAR !!!')
            else:
                print('YOU LOSE !!!')
    else:
        print('YOU LOSE!!!')

elif player==3:
    print('You chose door 3')
    print('DOOR 1 OPENED')
    player_choice=input('DO YOU WANT TO SWITCH?\nY/N')
    if player_choice=='Y' or player_choice=='y':
        choice2=int(input('SWITCH TO WHICH DOOR?\n2/3?'))
        if choice2==2:
            print('YOU WON THE CAR !!!')
        else:
            print('You chose door 3 ')
            print('DOOR 1 OPENED')
            player_choice=input('DO YOU WANT TO SWITCH?\nY/N')
            if player_choice=='Y' or player_choice=='y':
                print('YOU WON THE CAR !!!')
            else:
                print('YOU LOSE !!!')
    else:
        print('YOU LOSE!!!')

else:
    print('INVALID ENTRY')
    exit



    
    
    
