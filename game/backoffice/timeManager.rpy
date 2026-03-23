init python:
    def advanceTime(passDay=False):
        global time, day, tint
        currentTimeIndex = timesOfDay.index(time)
        lowerGlobals()

        if(passDay):
            nextDay()
            return

        if currentTimeIndex < len(timesOfDay) - 1:
            time = timesOfDay[currentTimeIndex + 1]
        else:
            nextDay()

        tint = "#7FA5F2" if time == "Night" or time == "Evening" else "#fff8b6"
    
    def nextDay():
        global time, day, tint
        time = timesOfDay[0]
        tint = "#fff8b6"
        currentTimeIndex = timesOfDay.index(time)
        currentDayIndex = daysOfWeek.index(day)
        if currentDayIndex < len(daysOfWeek) - 1:
            day = daysOfWeek[currentDayIndex + 1]
        else:
            day = daysOfWeek[0]

    def lowerGlobals():
        global hygiene, hunger
        hygiene = 0 if hygiene - 10 < 0 else hygiene - 10
        hunger = 100 if hunger + 10 > 100 else hunger + 10