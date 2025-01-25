# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nao = Character("Naoki")
define jos = Character("Josie")
define unknown = Character("???")
define baddie = Character("Abaddon")
define omi = Character("Naomi")

define e = Character("Eileen")

image Josie neutral = "images/Josie neutral.png"
image Abaddon neutral = "images/Abaddon neutral.png"
image Naomi neutral = "images/Naomi neutral.png"

# The game starts here.

label start:
    play music "placeholder_music.wav"

    menu:
        "Anyways, what do you choose?"

        "Good end!":
            window hide
            call minigame from _call_minigame
    
        "Bad end!":
            "!! WATCH OUT!"
            window hide
            pause 1.0
            call screen2show
            jump good_road

label good_road:
    scene bg black
    "You made the right choice!"
    return

label bad_road:
    scene bg black

    "You feel yourself losing consciousness... {w=3.0}{nw}"
    jump ending


