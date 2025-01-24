# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nao = Character("Naoki")
define jos = Character("Josie")
define unknown = Character("???")

# The game starts here.

label start:

    "Pop."

    "Such a simple sound."

    "But quite the same is said with such the nature of this allegory."

    "The residue of the bubble bursting lingers your mind, as you awake from a cold sweat."

    "Until now I can still hear it."

    "{i}Undeserving.{/i}"

    "... {w} Why did I even bother waking up today."

    "I drag my heavy body in the morning outside the door {w}to complete the debt that I owe to names unsaid."

    "Just then..."

    scene bg placeholder with fade

    show Josie neutral

    unknown "GOOOOODDD MORRRNNNINGG!!! HOW ARE YOU HONEYY?"

    "The voice is shrill, but this time I could tell. Something so sickeningly sweet can't be real."

    unknown "How was your nap? Damn, you look like a ghost!"

    unknown "You were always a little dead inside though, weren't you?"

    "In front of me was Josie. Shrewd though careless with her words, just like she'd always been."

    menu:

        "Anyways, what do you choose?"

        "Good end!":
            jump good_road
        
        "Bad end!":
            jump bad_road


label good_road:
    scene bg placeholder2
    "You made a good choice!"

    return

label bad_road:
    scene bg placeholder2

    "You screwed up."

    return

