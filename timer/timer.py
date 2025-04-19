import time

def get_user_input():
    while True:
        try:
            user_input = input('Insert Time to count down (h:m:s): ')
            parts = user_input.split(':')
            if len(parts) != 3:
                raise ValueError("Please enter time in h:m:s format.")
            hrs, mins, secs = map(int, parts)
            if hrs < 0 or mins < 0 or secs < 0:
                raise ValueError('Negrative Time values are not allowed ')

            total_seconds = hrs * 3600 + mins * 60 + secs
            return total_seconds
        except ValueError as e:
            print(f'Invalid input: {e}. Try again.')

def count_down(seconds:int):
    try:
        while seconds > 0:
            hrs_left = seconds // 3600
            mins_left = (seconds % 3600) //60
            secs_left = seconds % 60
            time.sleep(1)
            seconds -=1
            print(f'{hrs_left:02}:{mins_left:02}:{secs_left:02}')
        print("Time's up!")
    except KeyboardInterrupt:
        print("Countdown interrupted by user.")

 
print(count_down(get_user_input()))