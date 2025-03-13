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
    goal = 0

    while goal < 2 or one_shot < 1:

        x = player()

        if goal == 0 or goal == 1:
            if x == 4 or x == 5 or x == 6 or x == 8 or x == 9 or x == 10:
                goal = goal + 1
                print('Sum of Dices:', x, "| goal is", goal)
                if goal == 2:
                    print("GOAAAL Player wins ")
                    break
            elif x == 2 or x == 3 or x == 12:
                one_shot = one_shot + 1
                print('Sum of Dices:', x, '| The Casino Wins')
                break
            elif goal == 0 and (x == 7 or x == 11):
                one_shot = one_shot + 1
                print('Sum of Dices:', x, ' | Player has no goal, Lost')
                break
            elif goal == 1 and (x == 7 or x == 11):
                goal = goal + 1
                print('Sum of Dices:', x, '| goal is ', goal)
                print('Player Wins')
                break
    return 'End Game'


print(playing_rules())
