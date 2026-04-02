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
            action [Jump("reny_bedroom_interaction")]

label reny_bedroom_interaction:
    "You see Reny sitting on her bed, looking at her phone. She seems to be in a good mood, smiling at something on her screen."
    show reny default
    reny "Oh, hey there! I didn't see you come in. I'm just catching up on some messages. How's your day going?"

    menu:
        "Ask about her day":
            reny "It's been pretty good! I had a nice breakfast and then just relaxed for a bit. How about you?"
        "Compliment her outfit":
            show reny goofy
            reny "Aww, thanks! I just threw this on this morning. I'm glad you like it!"
        "Say goodbye":
            show reny thinking
            reny "Alright, see you around! Let me know if you want to hang out later."
    "You have a nice chat with Reny before she goes back to looking at her phone. You feel like you got to know her a little better."
    hide reny
    jump reny_bedroom