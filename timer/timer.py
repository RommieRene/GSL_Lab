import time

def user():
    user_input = input('Insert Time to count down (h:m:s): ')
    hrs, mins, secs = map(int, user_input.split(':'))
    total_seconds = hrs * 3600 + mins * 60 + secs
    return total_seconds


def count_down(seconds:int):
    while seconds > 0:
        hrs_left = seconds // 3600
        mins_left = (seconds % 3600) //60
        secs_left = seconds % 60
        time.sleep(1)
        seconds -=1
        print(f'{hrs_left:02}:{mins_left:02}:{secs_left:02}')
 
 
print(count_down(user()))