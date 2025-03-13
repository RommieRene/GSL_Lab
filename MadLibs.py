import random


def story_one():

    Data_story = {
        "Number": input("Enter a number: "),
        "Measure_of_time": input("Enter a measure of time hrs, days, years: "),
        "Mode_of_Transportation": input("Enter a mode of transportation: "),
        "Adjective": input("Enter an adjective: "),
        "Adjective2": input("Enter another adjective: "),
        "Noun": input("Enter a noun: "),
        "Color": input("Enter a color: "),
        "Part_of_the_Body": input("Enter a part of the body: "),
        "Verb": input("Enter a verb: "),
        "Number2": input("Enter another number: "),
        "Noun2": input("Enter another noun: "),
        "Noun3": input("Enter a noun: "),
        "Part_of_the_Body2": input("Enter another part of the body: "),
        "Verb2": input("Enter another verb: "),
        "Noun4": input("Enter a noun: "),
        "Adjective3": input("Enter another adjective: "),
        "Silly_Word": input("Enter a silly word: "),
        }

    story = [
        """
        It was about {Number} {Measure_of_time} ago when
        I arrived at the hospital in a{Mode_of_Transportation}.
        The hospital is a/an {Adjective} place, there are a lot of
        {Adjective2} {Noun} here. There are nurses here who have
        {Color} {Part_of_the_Body}.
        If someone wants to come into my room I told them that
        they have to {Verb} first.
        I have decorated my room with {Number2} {Noun2}.
        Today I talked to a doctor and they" were wearing
        a {Noun3} on their {Part_of_the_Body2}.
        I heard that all doctors {Verb2}
        {Noun4} every day for breakfast. The most {Adjective3}
        thing about being in the hospital
        is the {Silly_Word} {Noun}!"
        """
        ]

    story_str = " ".join(story).format(**Data_story)

    return print('Story One', story_str)


def story_two():

    Data_story = {
        "Number": input("Enter a number: "),
        "Number2": input("Enter a number: "),
        "Measure_of_time": input("Enter a measure of time hrs, days, years: "),
        "Adjective": input("Enter an adjective: "),
        "Adjective2": input("Enter another adjective: "),
        "Noun": input("Enter a noun: "),
        "Color": input("Enter a color: "),
        "Verb": input("Enter a verb: "),
        "Verb2": input("Enter another verb: "),
        "Silly_Word": input("Enter a silly word: "),
        "Proper_Noun": input("Enter a proper noun (person's name): "),
        "Animal": input("Enter an animal: "),
        "Verb3": input("Enter another verb: "),
        "Animal2": input("Enter another animal: "),
        "Adverb": input("Enter an adverb: "),
        "Noun2": input("Enter another noun: "),
    }

    story = [
        """
        This weekend I am going camping with {Proper_Noun}.
        I packed my lantern, sleeping bag, and {Noun}.
        I am so {Adjective} to {Verb} in a tent.
        I am {Adjective2} we might see a(n) {Animal},
        I hear they’re kind of dangerous.
        While we’re camping, we are going to hike, fish, and {Verb2}.
        I have heard that the {Color} lake is great for {Verb3}.
        Then we will {Adverb} hike through the
        forest for {Number} {Measure_of_time}.
        If I see a {Color} {Animal2} while hiking,
        I am going to bring it home as a pet!
        At night we will tell {Number2} {Silly_Word}
        stories and roast {Noun2} around the campfire!!
       """
    ]

    story_str = " ".join(story).format(**Data_story)

    return print('Story Two ', story_str)


def story_three():

    Data_story = {
        "Number": input("Enter a number: "),
        "Measure_of_time": input("Enter a measure of time hrs, days, years: "),
        "Adjective": input("Enter an adjective: "),
        "Adjective2": input("Enter another adjective: "),
        "Noun": input("Enter a noun: "),
        "Color": input("Enter a color: "),
        "Noun2": input("Enter another noun: "),
        "Noun3": input("Enter a noun: "),
        "Noun4": input("Enter a noun: "),
        "Adjective3": input("Enter another adjective: "),
        "Proper_Noun": input("Enter a proper noun (person's name): "),
        "Animal": input("Enter an animal: "),
        "Adjective4": input("Enter another adjective: "),
        "Adverb": input("Enter an adverb: "),
        "Place": input("Enter a place: "),
        "Magical_Creature": input("Enter a magical creature (plural): "),
        "Magical_Creature2": input("Enter a magical creature (plural): "),
        "Room_in_House": input("Enter a room in a house: "),
        "Verb_ing": input("Enter a verb ending in -ing: "),
        "Noun5": input("Enter a noun: "),
    }

    story = [
        """
        Dear {Proper_Noun}, I am writing to you from a {Adjective}
        castle in an enchanted forest.
        I found myself here one day after going for a
        ride on a {Color} {Animal} in {Place}.
        There are {Adjective2} {Magical_Creature}s and
        {Adjective3} {Magical_Creature2}s here!
        In the {Room_in_House} there is a pool full of {Noun}.
        I fall asleep each night on a {Noun2} of {Noun3}
        and dream of {Adjective4} {Noun4}.
        It feels as though I have lived here for
        {Number} {Measure_of_time}.
        I hope one day you can visit, although the only way
        to get here now is {Verb_ing} on a {Adjective2} {Noun5}!!
        """
    ]

    story_str = " ".join(story).format(**Data_story)

    return print('Story Three ', story_str)


def start_game():
    print("your story will start randomly")
    print("Number 1 -  Hospital story")
    print('Number 2 - Camping trip')
    print('Number 3 - Magical castle adventure')
    numbeer = input("Press Enter: ")
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
