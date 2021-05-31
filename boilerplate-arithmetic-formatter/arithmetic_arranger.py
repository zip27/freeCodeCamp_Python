import re 

def arithmetic_arranger(problems, solve = False):

  arranged_problems = ''

  # Error management
  if len(problems) > 5:
    return 'Error: Too many problems.'
  
  for prob in problems:
    if(len(re.findall('\s[/*]\s', prob)) > 0):
      return 'Error: Operator must be \'+\' or \'-\'.'
    
    if "+" in prob:
      opIndex = prob.index("+")
      isPlus = True
    elif "-" in prob:
      opIndex = prob.index("-")
      isPlus = False
    else:
      return 'Error: Operator must be \'+\' or \'-\'.'
 
    if(len(prob[0:(opIndex-1)]) > 4 or len(prob[(opIndex + 2):(len(prob))]) > 4):
      return 'Error: Numbers cannot be more than four digits.'

    if(len(re.findall('\D', prob)) > 3):
      return 'Error: Numbers must only contain digits.'

  # gets solutions if solve is true
  firstNum = list()
  secondNum = list()
  solutions = list()

  for prob2 in problems:

    if("+" in prob2):
      opIndex = prob2.index("+")
      isPlus = True
    else:
      opIndex = prob2.index("-")
      isPlus = False

    num1 = prob2[0:(opIndex-1)]
    num2 = prob2[(opIndex + 2):(len(prob2))]

    firstNum.append(num1)
    secondNum.append(num2)

    if(isPlus):
      solutions.append(int(num1) + int(num2))
    else:
      solutions.append(int(num1) - int(num2))

  # the first line 
  for i in range(len(firstNum)):
    if len(firstNum[i]) > len(secondNum[i]):
      lengthBig = len(firstNum[i])
    else:
      lengthBig = len(secondNum[i])
    
    dashLength = lengthBig + 2
    innerSpace = dashLength - len(firstNum[i])

    for r in range(innerSpace):
      arranged_problems += " "
    
    arranged_problems += firstNum[i]

    if i != (len(firstNum) - 1):
      for  q in range(4):
        arranged_problems += " "
    else:
      arranged_problems += "\n"

  # the second line
  for j in range(len(firstNum)):
    if("+" in problems[j]):
      arranged_problems += "+"
    else:
      arranged_problems += "-"
    
    if len(secondNum[j]) > len(firstNum[j]):
      opSpace = 1
    else:
      opSpace = 1 + (len(firstNum[j]) - len(secondNum[j]))
    
    for k in range(opSpace):
      arranged_problems += " "

    arranged_problems += secondNum[j]

    if j != (len(firstNum) - 1):
      for b in range(4):
        arranged_problems += " "
    else:
      arranged_problems += "\n"

  # the third line
  for x in range(len(firstNum)):
    if len(firstNum[x]) > len(secondNum[x]):
      dashLength = len(firstNum[x]) + 2
    else:
      dashLength = len(secondNum[x]) + 2
    
    for y in range(dashLength):
      arranged_problems += "-"
    
    if x != (len(firstNum) - 1):
      for z in range(4):
        arranged_problems += " "
    else:
      if solve:
        arranged_problems += "\n"
  
  # the fourth line 
  if solve:
    for c in range(len(firstNum)):
      if len(firstNum[c]) > len(secondNum[c]):
        dashLength = len(firstNum[c]) + 2
      else:
        dashLength = len(secondNum[c]) + 2

      lenSpace = dashLength - len(str(solutions[c]))

      for d in range(lenSpace):
        arranged_problems += " "

      arranged_problems += str(solutions[c])

      if c != (len(firstNum) - 1):
        for e in range(4):
          arranged_problems += " "

             
  return arranged_problems
