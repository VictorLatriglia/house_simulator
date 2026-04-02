label kitchen:
    show bg kitchen at ambient_light

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
            SetVariable("hunger", 0 if hunger - 20 <= 0 else hunger - 20),
            Function(advanceTime), Jump("kitchen")]
            
    $ show_reny = reny_schedule[day][time] == "kitchen"
    if(show_reny):
        imagebutton:
            idle "images/reny/kitchen/idle_light.png"
            hover "images/reny/kitchen/hover_light.png"
            xalign 0.85
            yalign 0.6
            action Jump("reny_kitchen_interaction")

label reny_kitchen_interaction:
    "You see Reny cooking something on the stove. She looks up and smiles when she sees you."
    show reny default
    reny "Oh, hey! I didn't expect to see you here. Just making some food. How's it going?"
    menu:
        "Ask about her cooking":
            reny "I like to cook! It's a nice way to relax and make something delicious. Do you like to cook?"
        "Compliment her cooking skills":
            show reny goofy
            reny "Aww, thanks! I do try to make good food. I'm glad you like it!"
        "Say goodbye":
            show reny thinking
            reny "Alright, see you around! Let me know if you want to hang out later."
    "You have a nice chat with Reny before she goes back to cooking. You feel like you got to know her a little better."
    hide reny
    jump kitchen