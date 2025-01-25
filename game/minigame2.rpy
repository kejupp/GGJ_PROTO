init python:
    import random
    screen_list = ["wheel","clutch", "accelerate", "break"]

    # def random_screen():
    #     q = random.randint(0,3)
    #     m = q
    #     return screen_list[q]

    trigger = True
    bounce = False

    class driver:
        def __init__(self):
            self.success = 0
            self.takeit = 0
            self.matchthis = 0

        def addh(self):
            self.success += 1

        def compare(self, a, b):
            if a == b:
                self.addh()
                return True
            else:
                return False

        def set_takeit(self, i):
            self.takeit = i

        def set_matchthis(self, i):
            self.matchthis = i
    
    car = driver()

# random called every time minigame is called

label screen2show:
        $ randomly = screen_list[1]
        $ trigger = True
        show screen minigame2
        pause 3
        $ trigger = False
        $ bounce = True
        pause 2
        $ bounce = False
        hide screen minigame2

        if car.takeit == 2:
            jump screen3show

        else:
            jump bad_road

label screen3show:
        $ randomly = screen_list[3]
        $ trigger = True
        show screen minigame2
        pause 3
        $ trigger = False
        $ bounce = True
        pause 2
        $ bounce = False
        hide screen minigame2

        if car.takeit == 4:
            return

        else:
            jump bad_road





        