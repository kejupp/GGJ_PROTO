# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    scene bg bathtub
    "Let's play the bubble-popping minigame."

<<<<<<< HEAD
    # Call the minigame label
    call minigame

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

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game. That's crazzyyy."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "This is more filler text. Huh."

    "This is a first person POV as well i guess."

    # This ends the game.
>>>>>>> parent of 9f3d4ea (Edited menu)

    "Game over."
    return
