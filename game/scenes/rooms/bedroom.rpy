label bedroom:
    
    show bg bedroom at ambient_light #at ambient_light

    call screen bedroom_screen

screen bedroom_screen:
    imagebutton:
        idle "images/gui/left_arrow.png"
        hover "images/gui/left_arrow_hover.png"
        xalign 0
        yalign 0
        action Call("travelMap", imagePath="bedroom")
    imagebutton:
        idle "images/house/buttons/bedroom/bed_idle.png"
        hover "images/house/buttons/bedroom/bed_hover.png"
        xalign 0.78
        yalign 0.9
        action [ Jump("dream_minigame")]