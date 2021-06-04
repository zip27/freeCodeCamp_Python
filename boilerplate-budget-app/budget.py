import math

class Category:
  catName = ''
  ledger = list()

  def __init__(self, name):
    self.catName = name
    self.ledger = []
  
  def deposit(self, amount, desc = ""):
    self.ledger.append({
      "amount": amount,
      "description": desc
    })

  def withdraw(self, amount, desc = ""):
    if self.check_funds(amount) is False:
      return False
    else:
      self.ledger.append({
        "amount": (-1 * amount),
        "description": desc
      })
      return True
  
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
  
  def get_balance(self):
    total_balance = 0
    for i in range(len(self.ledger)):
      total_balance += self.ledger[i]["amount"]
    return total_balance

  def transfer(self, amount, budgetCat):
    result = self.withdraw(amount, "Transfer to " + budgetCat.get_name())
    if result is False:
      return False
    else:
      budgetCat.deposit(amount, "Transfer from " + self.catName)
      return True

  def __str__(self):
    printer = ''

    # stars
    if len(self.catName) % 2 == 0:
      starLen = (30 - len(self.catName)) / 2
      for k in range(int(starLen)):
        printer += "*"
      printer += self.catName
      for k in range(int(starLen)):
        printer += "*"
      printer += "\n"
    else:
      starLen = int((30 - len(self.catName)) / 2)
      for k in range(starLen):
        printer += "*"
      printer += self.catName
      for k in range(starLen + 1):
        printer += "*"
      printer += "\n"

    # list
    for j in range(len(self.ledger)):
      if len(self.ledger[j]["description"]) > 23:
        desc = (self.ledger[j]["description"])[0:23]
      else:
        desc = self.ledger[j]["description"]
      printer += desc

      amountVal = self.add_zeros(str(self.ledger[j]["amount"]))

      inSpace = 30 - len(desc) - len(amountVal)
      for p in range(inSpace):
        printer += " "
      printer += amountVal + "\n"
    
    total = self.add_zeros(str(self.get_balance()))
    printer += "Total: " + total

    return printer

  def get_name(self):
    return self.catName
  
  def get_ledger(self):
    return self.ledger

  # helper method for adding zeros
  def add_zeros(self, amountVal):
      if "." not in amountVal:
        amountVal += ".00"
      elif amountVal.index(".") == len(amountVal) - 2:
        amountVal += "0"
      return amountVal

def create_spend_chart(categories):
  graph = ''

  # getting percentage values
  temp_spent = []
  pVal = []
  for a in categories:
    category_spent = 0
    for b in a.get_ledger():
      if b["amount"] < 0:
        category_spent += abs(b["amount"])
    temp_spent.append((a.get_name(), category_spent))

  # get sum of all withdrawals
  total_spent = 0
  for (f,g) in temp_spent:
    total_spent += g

  for (cat_name,withdraw) in temp_spent:
    percentVal = round_down((withdraw / total_spent) * 100) 
    pVal.append((cat_name, percentVal))

  graph += 'Percentage spent by category\n'

  # adding graph values to string
  for x in range(100, -10, -10):
    if x == 100:
      graph += str(x) + '|'
    elif x == 0:
      graph += '  ' + str(x) + '|'
    else:
      graph += ' ' + str(x) + '|'
    for (k,v) in pVal:
      if v >= x:
        graph += ' o '
      else:
        graph += '   '
    graph += '\n'
  
  # adding dashes
  dashLength = (len(pVal) * 3) + 1
  graph += '    '
  for y in range(dashLength):
    graph += "-"

  # finding longest category name
  large = len(pVal[0][0])
  for iter in range(1, len(pVal)):
    if len(pVal[iter][0]) > large:
      large = len(pVal[iter][0])
  
  # adding category names
  for iterator in range(large):
    graph += '\n     '
    for (name, value) in pVal:
      if iterator >= len(name):
        graph += '   '
      else:
        graph += name[iterator] + '  '

  


  return graph
  
  




def round_down(x):
    return int(math.floor(x / 10.0)) * 10

# Source: https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
# Source: https://www.codegrepper.com/code-examples/python/override+print+python+class
# Source: https://stackoverflow.com/questions/11040438/class-variables-is-shared-across-all-instances-in-python
# Source: https://stackoverflow.com/questions/26454649/python-round-up-to-the-nearest-ten 



