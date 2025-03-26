import random
import re


def v_input(prompt, is_number=False, is_word=False):

    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError('Input cannot be empty.')
            if is_number and not value.isdigit():
                raise ValueError('Please enter a valid number.')
            if is_word and not re.fullmatch(r"[A-Za-z\s]+", value):
                raise ValueError('pecial and Numeric Chars are invalid')
            return value
        except ValueError as e:
            print(f"Error: {e}")


def story_one():

    Data_story = {
        "Number": v_input('Enter a number :  ', is_number=True),
        "Measure_of_time": v_input('Enter hrs, days, years: ', is_word=True),
        "Transport": v_input('Enter transportation: ', is_word=True),
        "Adjective": v_input('Enter an adjective: ', is_word=True),
        "Adjective2": v_input('Enter another adjective: ', is_word=True),
        "Noun": v_input('Enter a noun: ', is_word=True),
        "Color": v_input('Enter a color: ', is_word=True),
        "body_part": v_input('Enter body Part: ', is_word=True),
        "Verb": v_input('Enter a verb: ', is_word=True),
        "Number2": v_input('Enter another number: ', is_number=True),
        "Noun2": v_input('Enter another noun: ', is_word=True),
        "Noun3": v_input('Enter a noun: ', is_word=True),
        "body_part2": v_input('another body part: ', is_word=True),
        "Verb2": v_input('Enter another verb: ', is_word=True),
        "Noun4": v_input('Enter a noun: ', is_word=True),
        "Adjective3": v_input('Enter another adjective: ', is_word=True),
        "Silly_Word": v_input('Enter a silly word: ', is_word=True),
    }

    story = f"""
    It was about {Data_story['Number']}
    {Data_story['Measure_of_time']} ago when
    I arrived at the hospital in a
    {Data_story['Transport']}.
    The hospital is a {Data_story['Adjective']}
    place, there are a lot of
    {Data_story['Adjective2']} {Data_story['Noun']}
    here. There are nurses here who have
    {Data_story['Color']} {Data_story['body_part']}.
    If someone wants to come into my room, I told them that
    they have to {Data_story['Verb']} first.
    I have decorated my room with
    {Data_story['Number2']} {Data_story['Noun2']}.
    Today I talked to a doctor and they were wearing
    a {Data_story['Noun3']} on their
    {Data_story['body_part2']}.
    I heard that all doctors {Data_story['Verb2']}
    {Data_story['Noun4']} every day for breakfast.
    The most {Data_story['Adjective3']}
    thing about being in the hospital
    is the {Data_story['Silly_Word']} {Data_story['Noun']}!
    """

    print('\nStory One:', story)


def story_two():

    Data_story = {
        "Number": v_input('Enter a number: ', is_number=True),
        "Number2": v_input('Enter a number: ', is_number=True),
        "Measure_of_time": v_input('Enter hrs, days, years: ', is_word=True),
        "Adjective": v_input('Enter an adjective: ', is_word=True),
        "Adjective2": v_input('Enter another adjective: ', is_word=True),
        "Noun": v_input('Enter a noun: ', is_word=True),
        "Color": v_input('Enter a color: ', is_word=True),
        "Verb": v_input('Enter a verb: ', is_word=True),
        "Verb2": v_input('Enter another verb: ', is_word=True),
        "Silly_Word": v_input('Enter a silly word: ', is_word=True),
        "Proper_Noun": v_input('proper noun(person`s name): ', is_word=True),
        "Animal": v_input('Enter an animal: ', is_word=True),
        "Verb3": v_input('Enter another verb: ', is_word=True),
        "Animal2": v_input('Enter another animal: ', is_word=True),
        "Adverb": v_input('Enter an adverb: ', is_word=True),
        "Noun2": v_input('Enter another noun: ', is_word=True)
    }

    story = f"""This weekend I am going camping with
    {Data_story['Proper_Noun']}
    I packed my lantern, sleeping bag,
    and {Data_story['Noun']}
    I am so {Data_story['Adjective']} to
    {Data_story['Verb']} in a tent.
    I am {Data_story['Adjective2']}
    we might see a(n) {Data_story['Animal']},
    I hear they're kind of dangerous.
    While we're camping, we are going to
    hike, fish, and {Data_story['Verb2']}.
    I have heard that the {Data_story['Color']}
    lake is great for {Data_story['Verb3']}.
    Then we will {Data_story['Adverb']} hike through the
    forest for {Data_story['Number']}
    {Data_story['Measure_of_time']}.
    If I see a {Data_story['Color']}
    {Data_story['Animal2']} while hiking,
    I am going to bring it home as a pet!
    At night we will tell {Data_story['Number2']}
    {Data_story['Silly_Word']}
    stories and roast {Data_story['Noun2']} around the campfire!!
    """

    print('\nStory Two:', story)


def story_three():

    Data_story = {
         "Number": v_input('Enter a number: ', is_number=True),
         "Measure_of_time": v_input('Enter hrs, days, years: ', is_word=True),
         "Adjective": v_input('Enter an adjective: ', is_word=True),
         "Adjective2": v_input('Enter another adjective: ', is_word=True),
         "Noun": v_input('Enter a noun: ', is_word=True),
         "Color": v_input('Enter a color: ', is_word=True),
         "Noun2": v_input('Enter another noun: ', is_word=True),
         "Noun3": v_input('Enter a noun: ', is_word=True),
         "Noun4": v_input('Enter a noun: ', is_word=True),
         "Adjective3": v_input('Enter another adjective: ', is_word=True),
         "Proper_Noun": v_input('proper noun(person`s name): ', is_word=True),
         "Animal": v_input('Enter an animal: ', is_word=True),
         "Adjective4": v_input('Enter another adjective: ', is_word=True),
         "Adverb": v_input('Enter an adverb: ', is_word=True),
         "Place": v_input('Enter a place: ', is_word=True),
         "Magiacal": v_input('magical creature(plural): ', is_word=True),
         "Magiacal2": v_input('magical creature(plural): ', is_word=True),
         "Room_in_House": v_input('Enter a room in a house: ', is_word=True),
         "Verb_ing": v_input('Enter a verb ending in -ing: ', is_word=True),
         "Noun5": v_input('Enter a noun:', is_word=True)
    }

    story = f"""
        Dear {Data_story['Proper_Noun']},
        I am writing to you from a {Data_story['Adjective']}
        castle in an enchanted forest.
        I found myself here one day after going for a
        ride on a {Data_story['Color']} {Data_story['Animal']}
        in {Data_story['Place']}.
        There are {Data_story['Adjective2']}
        {Data_story['Magiacal']}s and
        {Data_story['Adjective3']} {Data_story['Magiacal2']}s here!
        In the {Data_story['Room_in_House']}
        there is a pool full of {Data_story['Noun']}.
        I fall asleep each night on a
        {Data_story['Noun2']} of {Data_story['Noun3']}
        and dream of {Data_story['Adjective4']} {Data_story['Noun4']}.
        It feels as though I have lived here for
        {Data_story['Number']} {Data_story['Measure_of_time']}.
        I hope one day you can visit, although the only way
        to get here now is {Data_story['Verb_ing']} on
        a {Data_story['Adjective2']} {Data_story['Noun5']}!!
        """

    print('\nStory Three:', story)


def start_game():
    print('your story will start randomly')
    print('Number 1 -  Hospital story')
    print('Number 2 - Camping trip')
    print('Number 3 - Magical castle adventure')
    numbeer = input('Press Enter :  ')
    return numbeer


def starting():
    start = random.randint(1, 3)
    if start == 1:
        story_one()
    elif start == 2:
        story_two()
    else:
        if start == 3:
            story_three()


start_game()
starting()
