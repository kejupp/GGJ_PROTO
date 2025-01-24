# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("John")


# The game starts here.

label start:

    "...All we heard was a splash, then she was gone."

    scene bg placeholder with fade

    show sprite placeholder

    e "That was crazyyy"

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

