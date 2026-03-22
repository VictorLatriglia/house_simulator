label dream_minigame():
    show screen score_screen
    $ cont = 0 #continue variable
    $ sleep = 0 #sleep variable, increases with each successful qte hit, if it reaches 3, the player wins
    $ timerStart = 1
    $ timerInterval = 0.1

    "Click the Zzz in time to get some sleep! You need to successfully hit the button 3 times to have a good nap and advance time. You have 10 attempts!"

    #first attempt, to guarantee at least once
    call qte_setup(renpy.random.randint(1, 9) * 0.1, renpy.random.randint(2, 9) * 0.1)

    #while the player is successfully hitting the qte and sleep is less than 3
    #The player has 10 attempts before the minigame ends, regardless of success or failure, to prevent infinite loops in the case of very bad RNG
    while cont < 10 and sleep < 3: 
        call qte_setup(renpy.random.randint(1, 9) * 0.1, renpy.random.randint(2, 9) * 0.1)
        # to repeat the qte events until it is missed

    #screen must be hidden before the if statement, otherwise the final score will be displayed on the screen after the minigame ends, which looks weird
    hide screen score_screen

    if sleep >= 3:
        "You had a good nap! Time advanced to the next time of day."
        $ advanceTime(True)
    else:
        "You had a bad nap! Time did not advance."
        
    #regardless of win or lose, the player goes back to the bedroom
    jump bedroom

screen score_screen:
    text "Attempts: [10-cont]" xalign 0.99 yalign 1 style "gui"
    text "Sleep: [sleep]" xalign 0.99 yalign 0.05 style "gui"
                             
'''
"Function"/pseudo-function
calls the qte screen
parameters are:
    - amount of time given
    - total amount of time (is usually the same as above)
    - timer decreasing interval
    - the key/keyboard input to hit in the quick time event
    - the x alignment of the bar/box
    - the y alignment of the bar/box
'''
label qte_setup(x_align, y_align):

    $ time_start = timerStart
    $ interval = timerInterval
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_button
    # can change to call screen qte_button to switch to button mode
    # 1 if key was hit in time, 0 if key not
    $ sleep += _return
    $ cont += 1

    return

screen qte_button:
    #button press qte
    #if player presses anywhere but the button, it counts as a miss and returns 0
    #transparent.png is a 1920x1080 transparent image that covers the entire screen, allowing us to detect clicks outside of the button area
    button:
        action Return(0) #miss
        align 0.5, 0.5
        background "images/transparent.png"


    #if the timer runs out, it counts as a miss and returns 0
    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])

    vbox:
        xalign x_align yalign y_align spacing 25

        imagebutton:
            idle "images/gui/minigames/sleep/sleep.png"
            hover "images/gui/minigames/sleep/sleep_hover.png"
            action [Return(1)]
            xalign 0.5
            xysize 100, 100