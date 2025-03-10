import random

templates = [
    """
    It was about {Number} {Measure_of_time} ago when I arrived at the hospital in a {Mode_of_Transportation}. 
    The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. 
    There are nurses here who have {Color} {Part_of_the_Body}. 
    If someone wants to come into my room I told them that they have to {Verb} first. 
    I’ve decorated my room with {Number2} {Noun2}. 
    Today I talked to a doctor and they were wearing a {Noun3} on their {Part_of_the_Body2}. 
    I heard that all doctors {Verb2} {Noun4} every day for breakfast. 
    The most {Adjective3} thing about being in the hospital is the {Silly_Word} {Noun}!
    """,

    """
    This weekend I am going camping with {Proper_Noun}. I packed my lantern, sleeping bag, and {Noun}. 
    I am so {Adjective} to {Verb} in a tent. I am {Adjective2} we might see a(n) {Animal}, I hear they’re kind of 
    dangerous. 
    While we’re camping, we are going to hike, fish, and {Verb2}. 
    I have heard that the {Color} lake is great for {Verb3}. Then we will {Adverb} hike through the forest for {Number} 
    {Measure_of_time}. 
    If I see a {Color} {Animal2} while hiking, I am going to bring it home as a pet! 
    At night we will tell {Number2} {Silly_Word} stories and roast {Noun2} around the campfire!!
    """,

    """
    Dear {Proper_Noun}, I am writing to you from a {Adjective} castle in an enchanted forest. 
    I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. 
    There are {Adjective2} {Magical_Creature}s and {Adjective3} {Magical_Creature2}s here! 
    In the {Room_in_House} there is a pool full of {Noun}. 
    I fall asleep each night on a {Noun2} of {Noun3} and dream of {Adjective4} {Noun4}. 
    It feels as though I have lived here for {Number} {Measure_of_time}. 
    I hope one day you can visit, although the only way to get here now is {Verb_ing} on a {Adjective2} {Noun5}!!
    """
]
print("Choose a template for your story",
    "\nNumber 1 -  Hospital story",
    '\nNumber 2 - Camping trip',
    '\nNumber 3 - Magical castle adventure')
choice = int(input("Write the number fo your story: "))

template = templates[choice - 1]

data_of_story = {
    "Number" : int(input("Write a number: ")),
    "Number2" : str(input("Write another number: ")),
    "Measure_of_time" : str(input("Write a measure of time (hours, days, years): ")),
    "Mode_of_Transportation" : str(input("Write a mode of transportation: ")),
    "Adjective" : str(input("Write an adjective: ")),
    "Adjective2" : str(input("Write another adjective: ")),
    "Adjective3" : str(input("Write another adjective: ")),
    "Adjective4" : str(input("Write another adjective: ")),
    "Noun" : str(input("Write a noun: ")),
    "noun2" : str(input("Write another noun: ")),
    "noun3" : str(input("Write a noun: ")),
    "noun4" : str(input("Write a noun: ")),
    "Noun5" : str(input("Write a noun: "))
    "Color" : str(input("Write a color: ")),
    "Verb_ing" : str(input("Write a verb ending in -ing: ")),
    "Adverb" : str(input("Write an adverb: ")),
    "Verb" : str(input("Write a verb: ")),
    "verb2" : str(input("Write another verb: ")),
    "Part_of_the_Body" : str(input("Write a part of the body: ")),
    "Part_of_the_Body2" : str(input("Write another part of the body: ")),
    "Silly_Word" : str(input("Write a silly word: ")),
    "Proper_Noun" : str(input("Write a proper noun (person's name): ")),
    "Animal" : str(input("Write an animal: ")),
    "Animal2" : str(input("Write another animal: ")),
    "Feeling" : str(input("Write a feeling: ")),
    "Place" : str(input("Write a place: ")),
    "Magical_Creature" : str(input("Write a magical creature (plural): ")),
    "Room_in_House" : str(input("Write a room in a house: ")),
}

story = template.format(**data_of_story)

print("\n Your Story:\n")
print(story)