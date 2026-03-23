style gui:
    font "fonts/RobotoMono.ttf"
    color "#ffffff"
    size 40
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    
screen persistent_text:
    text "{image=images/gui/icons/hygiene.png} Hygiene: [hygiene]" pos (100, 10) style "gui"
    text "{image=images/gui/icons/food.png} Hunger: [hunger]" pos (100, 60) style "gui"
    text "{image=images/gui/icons/calendar.png} Day: [day], Time: [time]" pos (100, 110) style "gui"