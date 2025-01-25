# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
<<<<<<< HEAD
define nao = Character("Naoki")
define jos = Character("Josie")
define unknown = Character("???")
define baddie = Character("Abaddon")
define omi = Character("Naomi")
=======

define e = Character("Eileen")
>>>>>>> main

image Josie neutral = "images/Josie neutral.png"
image Abaddon neutral = "images/Abaddon neutral.png"
image Naomi neutral = "images/Naomi neutral.png"

# The game starts here.

label start:
<<<<<<< HEAD
    play music "placeholder_music.wav"

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

    show Naomi neutral

    unknown "GOOOOODDD MORRRNNNINGG!!! HOW ARE YOU HONEYY?"

    "The voice is shrill, but this time I could tell. Something so sickeningly sweet can't be real."

    unknown "How was your nap? Damn, you look like a ghost!"

    unknown "You were always a little dead inside though, weren't you?"

    "In front of me was Naomi. Shrewd though careless with her words, just like she'd always been."

    omi "Come on, come on! Everyone's waiting for us in the next room."

    "??? HOW DID YOU GUYS GET INTO MY HOUSE?"

    scene bg placeholder2 with fade

    show Abaddon neutral at right

    baddie "Well well well! If it isn't the drag of the party! Jeez, you're a mess!"

    "You WILL die. It's a canon event."

    baddie "Looking forward to see you try and kill me."

    show Josie neutral at left

    jos "Ohh, come on! Don't be such a meanie."

    "How are you even up lmao i thought you were catatonic."
=======
    scene bg bathtub
    "Let's play the bubble-popping minigame."
>>>>>>> main

<<<<<<< HEAD
    # Call the minigame label
    call minigame

<<<<<<< HEAD
    menu:

        "Anyways, what do you choose?"
=======
    jump after_minigame

label after_minigame:
    if bubble_game.bubbles_popped >= 12:
        "You popped all the bubbles!"
    else:
        "Time ran out."
=======
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
>>>>>>> main

        "Good end!":
            jump good_road
        
        "Bad end!":
            jump bad_road


label good_road:
    scene bg black
    "You made a good choice!"

    "Game over."
    return

label bad_road:
    scene bg black

    "You screwed up."

    jump ending


