import random

one_shot = 0
goal = 0

while goal < 2 and one_shot < 1:

    num1 = random.randint(1,7)
    num2 = random.randint(1,7)
    sum = num1 + num2

    if sum == 2 or sum == 3 or sum == 12:
        one_shot = one_shot + 1

        print('the sum is ', sum, 'The Casino Wins')

    elif goal == 0 and sum == 4 or sum == 5 or sum == 6 or sum == 8 or sum == 9 or sum == 10:
        goal = goal + 1

        print('the sum is ', sum, "goal is", goal)

        if goal == 2:
            print("GOAAAL Congratulations to the Player"
                  "\n Player wins ")

    elif goal == 0 and sum == 7 or sum == 11:
        one_shot = one_shot + 1

        print('the sum is ', sum, 'Player Lost')

    elif goal == 1 and (sum == 7 or sum == 11):
        goal = goal + 1

        print('the sum is ', sum, 'goal is ', goal, 'Player Wins ')
    else:
        break