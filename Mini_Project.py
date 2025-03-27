import random


def diceOne():
    diceOne = random.randint(1, 6)
    return int(diceOne)


def diceTwo():
    diceTwo = random.randint(1, 6)
    return int(diceTwo)


def roll_the_dice(x, y) -> int:
    sum_of_dice = int(y) + int(x)
    return int(sum_of_dice)


def player():
    input('Press Enter to roll the dices')
    
    return int(roll_the_dice(diceOne(), diceTwo()))


def playing_rules():
    one_shot = 0
    point = 0
    goal_num = 0
    while point < 2 and one_shot < 1:

        x = player()
        goal_num += x
        if (x == 4 or x == 5 or x == 6 or x == 8 or x == 9 or x == 10) and point == 0:
            point += 1
            print('Point', point, 'Dice gives', x, 'Your goal number is', goal_num)
            print('-------------')            

        elif point == 1 and (x == 4 or x == 5 or x == 6 or x == 8 or x == 9 or x == 10):
            goal_num = goal_num - x
            print('Dice gives',x,'your goal number is', goal_num)
            if goal_num == x:
                point += 1
                print("Point", point, 'your goal number is', goal_num, 'PLAYER WINS')
                print('-------------')            
                
        
        elif x == 2 or x == 3 or x == 12:
            print('Point' ,point, 'Craps, CASINO WINS', "Dice gave", x)
            one_shot += 1
            
        
        elif point == 0 and (x == 7 or x == 11):
            one_shot += 1
            print('Point', point, 'Player lost :( Dice gave', x, 'yout goal number was', goal_num)
            
        
        elif point > 0 and (x == 7 or x == 11):
            point += 1
            print("Point", point, 'PLAYER WINS', x, 'your goal number was', goal_num)
            print('-------------')            

    return 'End Game'


print(playing_rules())
