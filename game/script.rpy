# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image bg bedroom = "images/house/bedroom.png"
image bg bathroom = "images/house/bathroom.png"
image bg kitchen = "images/house/kitchen.png"

define hygiene = 0
define hunger = 100

define time = "Morning"
define day = "Monday"

define daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
define timesOfDay = ["Morning", "Afternoon", "Evening", "Night"]

# The game starts here.

label start:
    show screen persistent_text
    jump bedroom
