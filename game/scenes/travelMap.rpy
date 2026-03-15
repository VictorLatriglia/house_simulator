label travelMap(imagePath):
    scene expression "bg " + imagePath
    "You are in the [imagePath]. Where do you want to go?"
    menu:
        "Go to the bathroom" if imagePath != "bathroom":
            jump bathroom
        "Go to the kitchen" if imagePath != "kitchen":
            jump kitchen
        "Go to the bedroom" if imagePath != "bedroom":
            jump bedroom
        "Stay here":
            jump expression imagePath