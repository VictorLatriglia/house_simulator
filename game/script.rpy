# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image bg bedroom = "images/house/bedroom.png"
image bg bathroom = "images/house/bathroom.png"
image bg kitchen = "images/house/kitchen.png"
image bg reny_bedroom = "images/house/renys_room.png"

define hygiene = 0
define hunger = 100

define time = "Morning"
define day = "Monday"
define tint = "#fff8b6"

define daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
define timesOfDay = ["Morning", "Afternoon", "Evening", "Night"]

define reny_schedule = {
    "Monday": {
        "Morning": "kitchen",
        "Afternoon": "reny_bedroom",
        "Evening": "bathroom",
        "Night": "reny_bedroom"
    },
    "Tuesday": {
        "Morning": "bathroom",
        "Afternoon": "kitchen",
        "Evening": "reny_bedroom",
        "Night": "reny_bedroom"
    },
    "Wednesday": {
        "Morning": "reny_bedroom",
        "Afternoon": "bathroom",
        "Evening": "kitchen",
        "Night": "reny_bedroom"
    },
    "Thursday": {
        "Morning": "kitchen",
        "Afternoon": "reny_bedroom",
        "Evening": "bathroom",
        "Night": "reny_bedroom"
    },
    "Friday": {
        "Morning": "bathroom",
        "Afternoon": "kitchen",
        "Evening": "reny_bedroom",
        "Night": "reny_bedroom"
    },
    "Saturday": {
        "Morning": "reny_bedroom",
        "Afternoon": "bathroom",
        "Evening": "kitchen",
        "Night": "reny_bedroom"
    },
    "Sunday": {
        "Morning": "kitchen",
        "Afternoon": "reny_bedroom",
        "Evening": "bathroom",
        "Night": "reny_bedroom"
    }
}

# The game starts here.

transform ambient_light:
    matrixcolor TintMatrix(tint)

label start:
    show screen persistent_text
    play music "audio/main_loop.wav" loop volume 0.5
    jump bedroom
