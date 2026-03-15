label bathroom:
    scene bg bathroom

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
        SetVariable("hygiene", hygiene + 20)]