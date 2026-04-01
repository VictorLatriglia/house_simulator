label reny_bedroom:
    show bg reny_bedroom at ambient_light

    call screen reny_bedroom_screen

screen reny_bedroom_screen:
    imagebutton:
        idle "images/gui/right_arrow.png"
        hover "images/gui/right_arrow_hover.png"
        xalign 0.9999  # Why does this stupid thing not work with 1?
        yalign 0
        action Call("travelMap", imagePath="reny_bedroom")

    $ show_reny = reny_schedule[day][time] == "reny_bedroom"
    if(show_reny):
        imagebutton:
            idle "images/reny/reny_bedroom/idle.png"
            hover "images/reny/reny_bedroom/hover.png"
            xcenter 0.35
            yalign 0.70
            action Notify("HI!")