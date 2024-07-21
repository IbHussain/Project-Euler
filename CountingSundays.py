daysList = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def runDays(leap, firstDay, daysList, year):
    leapList = ['1','32','61','92','122','153','183','214','245','275','306','336']
    nonLeapList = ['1','32','60','91','121','152','182','213','244','274','305','335']
    currentDay = firstDay
    totalSundaysOnFirst = 0
    if leap == True:
        days = 367 #366
    else:
        days = 366 #365
    #run the days
    for day in range(1, days):
        currentDay += 1
        currentDay %= 7

        #check if days are first and sunday
        #leap year check

        if leap == True:
            for d in leapList:
                if day == int(d):
                    if currentDay == 6:
                        totalSundaysOnFirst += 1
        else:
            for d in nonLeapList:
                if day == int(d):
                    if currentDay == 6:
                        totalSundaysOnFirst += 1
                
    #Get the current day for the next year
    return currentDay, totalSundaysOnFirst

trueTotalSundaysOnFirst = 0
leap = False
firstDay = 1
for year in range(1901, 2001): #2001
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    else:
        leap = False
    firstDayPass, totalSunAdd = runDays(leap, firstDay, daysList, year)
    trueTotalSundaysOnFirst = trueTotalSundaysOnFirst + totalSunAdd
    firstDay = firstDayPass

print(trueTotalSundaysOnFirst)
