init python:
    import random
    screen_list = ["wheel","clutch", "accelerate", "break"]

    trigger = True
    bounce = False

    def random_screen():
        q = random.randint(0,3)
        return screen_list[q]

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
        "!! WATCH OUT! {w=3}{nw}"
        pause 0.3
        $ randomly = random_screen()
        show screen minigame2
        pause 1 
        $ bounce = True
        pause 3
        $ bounce = False
        hide screen minigame2

        if car.compare(car.takeit, car.matchthis) == True:
            $ car.addh()
            
            $ car.takethis = 0
            $ car.matchthis = 0

            jump screen3show
        elif car.compare(car.takeit, car.matchthis)  == False:
            jump bad_road

label screen3show:
        $ randomly = random_screen()
        show screen minigame2
        pause 1 
        $ bounce = True
        pause 3
        $ bounce = False
        hide screen minigame2

        if car.compare(car.takeit, car.matchthis) == True:
            $ car.addh()

            $ car.takethis = 0
            $ car.matchthis = 0
            jump screen4show
        elif car.compare(car.takeit, car.matchthis) == False:
            jump bad_road

label screen4show:
        show screen minigame2
        pause 1 
        pause 3
        hide screen minigame2

        if car.compare(car.takeit, car.matchthis) == True:
            $ car.addh()

            $ car.takethis = 0
            $ car.matchthis = 0
            
            return
        elif car.compare(car.takeit, car.matchthis) == False:
            jump bad_road





        