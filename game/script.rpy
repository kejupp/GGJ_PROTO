# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define nao = Character("Naoki")
define jos = Character("Josie")
define unknown = Character("???")
define bad = Character("Kitarou")
define omi = Character("Naomi")

image Naoki neutral = "images/Naoki neutral.png"
image Kitarou neutral = "images/Kitarou neutral.png"
image Naomi neutral = "images/Naomi neutral.png"
image Naoki surprised = "images/Naoki surprised.png"
image Kitarou annoyed = "images/Kitarou annoyed.png"
image Naomi excited = "images/Naomi excited.png"

# The game starts here.

label start:
    play music "placeholder_music.wav"

    scene bg black

    "Regret and remorse. They can both come hand in hand as a pair, but that doesnt mean they should."
    "Coincidence and circumstance."
    "Appearing so sudden I swear that I can see flashes of a different life in each one."
    "{i}Pop.{i}"
    "Just like that."
    "Like a bad dream you once had, burst into reality without your permission."
    "Even today I can still hear it."
    "..."
    "...{w}Today is just another day once again.{w}"
    "Even walking the morning steps is just a reminder that I am to walk for someone who isn't here anymore"
    "It's heavy."
    "..."

    "Why do I hear footsteps?"
    
    "{i}Rapid light footsteps echo across the house, followed by someone with rosy cheeks and bubbly attire.{/i}{w=4}{nw}"

    show Naomi excited at center with moveinleft
    omi "{b} Good Morning!!!{/b} How are you, honey?"

    scene bg kitchen

    "{i}Her petite stature peeks through under the door frame.{i}"

    show Naomi excited with fade:
        yalign 1


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


