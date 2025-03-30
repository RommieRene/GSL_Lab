#Timer 

program takes the time from the user as a timer and start to countdown in the terminal - each new countdown line appears after one second, not immediately


**user()** Function prompts the user to input a time in the format h:m:s (hours:minutes:seconds), then converts that time into total seconds for easier countdown calculation.
1. Prompting User for Input:

    The function asks the user to input a time in the format h:m:s. For example, 0:5:30 represents 0 hours, 5 minutes, and 30 seconds.
2. Parsing the Input:

    The user input is split into hours, minutes, and seconds using split(':'). This splits the string into a list of values based on the colon separator. 
3. Converting to Integer:

    The map(int, ...) function converts the individual components (hours, minutes, and seconds) from    strings to integers.
4. Calculating Total Seconds:

    The function calculates the total time in seconds by converting the hours to seconds (hrs * 3600), the minutes to seconds (mins * 60), and then adding the remaining seconds (secs).
5. Returning Total Seconds:

    Finally, the function returns the total number of seconds as an integer, which can be used for further countdown calculations.

**count_down(seconds: int)** function accepts a number of seconds as input and performs a countdown, displaying the remaining time in the format hh:mm:ss. The countdown is updated every second, showing the hours, minutes, and seconds left until the timer reaches zero.

1. Accepting Input:

    The function takes an integer seconds as its input parameter, which represents the total time to count down from, in seconds.
2. Countdown Loop:

    A while loop runs as long as seconds is greater than zero. In each iteration of the loop:

    The function calculates the remaining hours, minutes, and seconds:

    hrs_left = seconds // 3600: Calculates the number of hours left by dividing the total seconds by 3600 (the number of seconds in one hour).

    mins_left = (seconds % 3600) // 60: Calculates the number of minutes left after removing the hours.
    
    secs_left = seconds % 60: Calculates the remaining seconds after removing the full minutes.
3. Sleeping for 1 Second:

    time.sleep(1) pauses the program for 1 second, creating the effect of real-time countdown.
4. Decreasing Time:

    After displaying the time, the seconds variable is reduced by 1 (seconds -= 1), so the countdown continues to the next second.
5. Displaying Remaining Time:

    The countdown is displayed in the format hh:mm:ss, using the print() function.

    The format f'{hrs_left:02}:{mins_left:02}:{secs_left:02}' ensures that each value (hours, minutes, and seconds) is always displayed with two digits. For example, 01:09:05 instead of 1:9:5.
6. Stopping the Countdown:

    The loop exits when seconds reaches zero, and the countdown stops.
