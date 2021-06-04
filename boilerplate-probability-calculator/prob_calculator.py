import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = []
    def __init__(self, **kwargs):
        self.contents = []
        for (key, value) in kwargs.items():
            for i in range(value):
                self.contents.append(key)


    def draw(self, numDraw, replace = None):

        if replace:
            tempList = copy.deepcopy(self.contents)

        drawRes = []
        if numDraw > len(self.contents):
            return self.contents
        for j in range(numDraw):
            drawRes.append(self.contents.pop(random.randint(0, (len(self.contents) - 1))))

        if replace:
            self.contents = tempList
            tempList = []

        return drawRes

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    validRuns = 0
    nescBalls = []

    for (k,v) in expected_balls.items():
        for p in range(v):
            nescBalls.append(k)

    for k in range(num_experiments):

        result = hat.draw(num_balls_drawn, True)

        if list_in_list(nescBalls, result):
            validRuns += 1

    return validRuns / num_experiments

# checks if list1 is in list2 (helper method)
def list_in_list(list1, list2):
  removeNumber = 0
  tempList2 = copy.deepcopy(list2)
  for elem in list1:
    for part in tempList2:
      if part == elem:
        tempList2.remove(elem)
        removeNumber += 1
        break
  if (removeNumber == len(list1)):
    return True
  else:
    return False

# Source 1: https://www.geeksforgeeks.org/args-kwargs-python/
# Source 2: https://pynative.com/python-random-randrange/
# Source 3: https://stackoverflow.com/questions/17873384/how-to-deep-copy-a-list

