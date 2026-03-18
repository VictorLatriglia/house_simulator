label kitchen:
    scene bg kitchen

    call screen kitchen_screen

screen kitchen_screen:
    imagebutton:
        idle "images/gui/right_arrow.png"
        hover "images/gui/right_arrow_hover.png"
        xalign 0.9999  # Why does this stupid thing not work with 1?
        yalign 0
        action Call("travelMap", imagePath="kitchen")
    imagebutton:
        idle "images/house/buttons/kitchen/kitchen_idle.png"
        hover "images/house/buttons/kitchen/kitchen_hover.png"
        xcenter 0.497
        yalign 0.368
        action [Notify("You ate some food! Hunger -20") ,
            SetVariable("hunger", hunger - 20),
            Function(advanceTime)]