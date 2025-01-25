# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")


# The game starts here.

label start:
    scene bg bathtub
    "Let's play the bubble-popping minigame."

    # Call the minigame label
    call minigame

    jump after_minigame

label after_minigame:
    if bubble_game.bubbles_popped >= 12:
        "You popped all the bubbles!"
    else:
        "Time ran out."

    "Game over."
    return
