init python:
    def leave():
        quit()


label struggle:
    "Giving up already? Typical. Fine, have it your way. {w=3.0}{nw}"
    call screen credits

label end_now:
    $ leave()

transform credits_scroll(speed):
    xcenter 0.5 yanchor 0.0 ypos 1.0
    ypos 600
    linear speed ypos -66000

screen credits():

    add "bg black.png"

    ## Ensure that the game_menu screens can't be stopped
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "mouseup_3" action NullAction()

    style_prefix "credits"

    timer 5 action Jump("end_now") #46.5 seconds
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(80.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            label "Credits" xalign 0.5
            null height 75
            label "Producer" xalign 0.5
            null height 75
            text "BadMustard"
            null height 10
            text "redacted"
            null height 10
            text "redacted"
            null height 10
            text "redacted"


style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    text_align 0.5

style credits_label_text:
    xalign 0.5
    justify True
    size 125
    text_align 0.5
    color "#ff0000"

style credits_text:
    xalign 0.5
    size 60
    justify True
    text_align 0.5
    color "#ffffff"
