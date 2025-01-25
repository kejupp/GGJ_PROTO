init python:
    import random

    bubble_list = []

    def spawn_bubble():
        global bubble_list
        new_bubble = ({
            "x": random.randint(100, 600),  # Randomize X position
            "y": 800  # Start from the bottom of the screen
        })

        for bubble in bubble_list:
                if abs(new_bubble["x"] - bubble["x"]) < 50:  # Minimum spacing
                    return  # Skip this spawn if too close

        bubble_list.append(new_bubble)
    
    def remove_bubble(index):
        global bubble_list
        del bubble_list[index]


    class BubbleMinigame:
        def __init__(self):
            self.bubbles_popped = 0
            self.max_bubbles = 12
            self.time_limit = 30 # seconds
            self.game_over = False
            self.start_time = None

        def start_game(self):
            self.bubbles_popped = 0
            self.start_time = renpy.get_game_runtime()
            self.game_over = False

        def update_timer(self):
            if renpy.get_game_runtime() - self.start_time >= self.time_limit:
                self.game_over = True

        def pop_bubble(self):
            self.bubbles_popped += 1
            if self.bubbles_popped >= self.max_bubbles:
                self.game_over = True

    bubble_game = BubbleMinigame()

label minigame:
    $ bubble_game.start_game()
    show screen bubble_minigame
    $ renpy.pause(30, hard=True)
    hide screen bubble_minigame
    return

transform bubble_move(x, y):
    xpos x
    ypos y
    linear 5.0 ypos -100  # Move the bubble upwards over 5 seconds