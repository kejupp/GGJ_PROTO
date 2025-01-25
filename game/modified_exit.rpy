init python:
    def leave():
        quit()


label struggle:
    call screen quit_cg 

screen quit_cg():
    timer 1 action Jump("dialog")

label dialog:
    $ renpy.call_screen("dialog", "Taking the easy way out I see. Go on then.")


label screen_die:
    $ leave()

label after_endcg:
    call screen dead

screen dead:
    add "placeholder cg"
    timer 3 action Jump("end_now")


screen dialog(message):
    modal True
    zorder 200
    style_prefix "confirm"
    add "bg black"

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5

    timer 5 action Jump("after_endcg")
    

label ending:
    # "Giving up already? Typical. Fine, have it your way. {w=3.0}{nw}"
    call screen credits

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

    timer 5 action Return() #46.5 seconds
    ## Adjust this number to control when the Credits screen is hidden and the game
    ## returns to its normal flow.

    frame at credits_scroll(90.0): #bigger is slower
        ## Adjust this number to control the speed at which the credits scroll.
        background None
        xalign 0.5

        vbox:
            text "Made by"
            null height 75
            text "Team Milktea Fettuccine"
            null height 10
            text "For the Global Game Jam 2025"
            null height 10


            text "Programmers"
            null height 75
            text "redacted"
            null height 10

            text "Artists"
            null height 10
            text "redacted"
            null height 10

            text "Writers"
            null height 10
            text "redacted"
            null height 10

            text "Music and Sound design"
            null height 10
            text "redacted"
            null height 10


style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    text_align 0.5

style credits_text:
    xalign 0.5
    size 60
    justify True
    text_align 0.5
    color "#ffffff"

label end_now:
    $ leave()
