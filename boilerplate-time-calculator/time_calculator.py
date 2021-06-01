def add_time(start, duration, weekday = ""):
  
  weekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
  'Friday', 'Saturday', 'Sunday']
  decider = False

  colonIndex = start.index(":")
  if "AM" in start:
    periodIndex = start.index("AM")
    isPM = False
  else:
    periodIndex = start.index("PM")
    isPM = True
    

  startHours = int(start[0:colonIndex])
  startMinutes = int(start[(colonIndex+1):periodIndex])

  if isPM and (startHours >= 1):
    startHours += 12

  # express the duration in terms of integer minutes
  colonIndex2 = duration.index(":")
  durHours = int(duration[0:colonIndex2])
  durMinutes = int(duration[(colonIndex2+1):len(duration)])

  endHours = startHours
  endMinutes = startMinutes
  numDays = 0

  for k in range(durHours):
      if endHours == 24:
        numDays += 1
        endHours -= 23
      else:
        endHours += 1

  if (startMinutes + durMinutes) > 59:
    endHours += 1
    endMinutes = durMinutes - (60 - startMinutes)
    if endHours == 24:
      numDays += 1
      endHours = 12
      decider = True
  else:
    endMinutes += durMinutes
  
  # formatting section
  if endMinutes < 10:
    stringMin = "0" + str(endMinutes)
  else:
    stringMin = str(endMinutes)

  if endHours > 12:
    endHours -= 12
    new_time = str(endHours) + ":" + stringMin + " PM" 
  elif endHours == 12 and decider:
    new_time = str(endHours) + ":" + stringMin + " AM" 
  elif endHours == 12 and not decider:
    new_time = str(endHours) + ":" + stringMin + " PM" 
  else: 
    new_time = str(endHours) + ":" + stringMin + " AM" 

  if len(weekday) > 0:
    weekday = weekday.lower()
    weekday = weekday[0].upper() + weekday[1:len(weekday)]
    weekIndex = weekList.index(weekday)

    if weekIndex + numDays >= len(weekList):
      if weekIndex == 0:
          weekIndex += (numDays % 7)
          new_time += ", " + weekList[weekIndex]
      else:
          toMonday = len(weekList) - weekIndex
          weekIndex = ((numDays - toMonday) % 7)
          new_time += ", " + weekList[weekIndex]
    else:
      new_time += ", " + weekList[weekIndex + numDays]
  
  if numDays == 1:
    new_time += " (next day)"
  elif numDays > 1:
    new_time += " (" + str(numDays) + " days later)"

  return new_time

  '''
  Sources: https://www.freecodecamp.org/news/mathematics-converting-am-pm-to-24-hour-clock/

  hours first approach
  60, 43, 20

  '''