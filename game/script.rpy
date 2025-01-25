# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nao = Character("Naoki")
define jos = Character("Josie")
define unknown = Character("???")
define baddie = Character("Abaddon")
define omi = Character("Naomi")

image Josie neutral = "images/Josie neutral.png"
image Abaddon neutral = "images/Abaddon neutral.png"
image Naomi neutral = "images/Naomi neutral.png"

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

    jos "Come on, come on! Everyone's waiting for us in the next room."

    "??? HOW DID YOU GUYS GET INTO MY HOUSE?"

    scene bg placeholder2 with fade

    show Abaddon neutral at right

    baddie "Well well well! If it isn't the drag of the party! Jeez, you're a mess!"

    "You WILL die. It's a canon event."

    baddie "Looking forward to see you try and kill me."

    show naomi neutral at left

    omi "Ohh, come on! Don't be such a meanie."

    "ONG I will probably snap at you too."


    menu:

        "Anyways, what do you choose?"

        "Good end!":
            jump good_road
        
        "Bad end!":
            jump bad_road


label good_road:
    scene bg black
    "You made a good choice!"

    return

label bad_road:
    scene bg black

    "You screwed up."

    return


