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