init python:
    def advanceTime(passDay=False):
        global time, day
        currentTimeIndex = timesOfDay.index(time)
        lowerGlobals()

        if(passDay):
            nextDay()
            return

        if currentTimeIndex < len(timesOfDay) - 1:
            time = timesOfDay[currentTimeIndex + 1]
        else:
            nextDay()
    
    def nextDay():
        global time, day
        time = timesOfDay[0]
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