init python:
    import random
    screen_list = ["wheel","clutch", "accelerate", "breaks"]

    def random_screen():
        q = random.randint(0,3)
        return screen_list[q]


label screen2show:
        show screen vehicle
        pause 0.5
        hide screen vehicle
        pause 0.3
        show screen minigame2
        pause 0.7
        hide screen minigame2
        pause 0.5
        show screen vehicle