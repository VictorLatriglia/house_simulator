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
        Function(advanceTime), Jump("bathroom")]
        
    $ show_reny = reny_schedule[day][time] == "bathroom"
    if(show_reny):
        imagebutton:
            idle im.Scale("images/reny/bathroom/idle.png", 400, 1000)
            hover im.Scale("images/reny/bathroom/hover.png", 400, 1000)
            xcenter 0.23
            yalign 0.9
            action Jump("reny_bathroom_interaction")

label reny_bathroom_interaction:
    "You see Reny brushing her teeth in front of the bathroom mirror. She looks up and smiles when she sees you."
    show reny default
    reny "Oh, hey! I didn't expect to see you here. Just getting ready for the day. How's it going?"

    menu:
        "Ask about her morning routine":
            reny "Well, I usually start with brushing my teeth and washing my face. Then I might take a shower if I have time. What about you?"
        "Compliment her smile":
            show reny goofy
            reny "Aww, thanks! I do try to keep my teeth clean. I'm glad you like my smile!"
        "Say goodbye":
            show reny thinking
            reny "Alright, see you around! Let me know if you want to hang out later."
    "You have a nice chat with Reny before she goes back to brushing her teeth. You feel like you got to know her a little better."
    hide reny
    jump bathroom