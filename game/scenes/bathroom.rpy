label bathroom:
    show bg bathroom at ambient_light

    call screen bathroom_screen

screen bathroom_screen:
    imagebutton:
        idle "images/gui/left_arrow.png"
        hover "images/gui/left_arrow_hover.png"
        xalign 0
        yalign 0
        action Call("travelMap", imagePath="bathroom")

    imagebutton:
        idle "images/house/buttons/bathroom/shower_idle.png"
        hover "images/house/buttons/bathroom/shower_hover.png"
        xcenter 0.78
        yalign 1
        action [Notify("You took a shower! Hygiene +20") ,
        SetVariable("hygiene",100 if hygiene + 20 >= 100 else hygiene + 20),
        Function(advanceTime), Jump("kitchen")]
    
    imagebutton:
        idle im.Scale("images/reny/bathroom/idle.png", 400, 1000)
        hover im.Scale("images/reny/bathroom/hover.png", 400, 1000)
        xcenter 0.23
        yalign 0.9
        action Notify("HI!")