import sys, time
from getkey import keys, getkey
from os import system, name
from time import sleep
import linecache as lc

global location, hasPastInfo, health, endurance, strength, agility, intelligence, luck, confidence, charisma, carryweight, s1, s2, s3

# Save class
class save():
  def __init__(self, filename, dataLine, name):
        self.filename = filename
        self.dataLine = dataLine
        self.name = name
  def exists(self):
    if lc.getline("saveInfo.txt", self.dataLine).rstrip() == "True":
      lc.clearcache()
      return "True"
    else:
      lc.clearcache()
      return "False"

s1 = save("s1.txt", 3, "s1")
s2 = save("s2.txt", 6, "s2")
s3 = save("s3.txt", 9, "s3")

BOLD = "\033[1m"
CLEAR = "\033[0m"

def clear():
     # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def initGame():
  global location, hasPastInfo, health, endurance, strength, agility, intelligence, luck, confidence, charisma, carryweight
  location = ""
  hasPastInfo = False
  health = 1
  endurance = 1
  strength = 1
  agility = 1
  intelligence = 1
  luck = 1
  confidence = 1
  charisma = 1
  carryweight = 3
  return

def setLocation(new_location):
  global location
  location = new_location
  return

def selection(title, optionList, x=0, y=0):
  clear()
  selectionIndex = 1

  typingPrint(title + "\n")
  for option in optionList:
    if optionList.index(option) + 1 == selectionIndex: typingPrint(BOLD + option + CLEAR)
    else: typingPrint(option)
  while True:
    clear()
    print(title + "\n")
    for option in optionList:
      if optionList.index(option) + 1 == selectionIndex: print(BOLD + option + CLEAR)
      else: print(option)

    key = getkey()
    match key:
      case keys.UP:
        selectionIndex -= 1
      case keys.DOWN:
        selectionIndex += 1
    
    if selectionIndex <= 0: selectionIndex = len(optionList)
    elif selectionIndex > len(optionList): selectionIndex = 1

    if key == keys.ENTER: return selectionIndex
    if key == keys.ESC and x == 0: return "esc"
    if key == keys.BACKSPACE and y == 1: return f"delete: {selectionIndex}"

def pauseMenu():
  clear()
  Choice = selection("Paused game", ["Resume game", "Save game", "Load game", "Exit to main menu"], 1)
  match Choice:
    case 1: return
    case 2: saveMenu()
    case 3: loadMenu()
    case 4: exitToMenu()
  pauseMenu()

def exitToMenu():
  clear()
  Choice = selection("You will lose any unsaved progress. Continue?", ["Yes.", "No."], 1)
  
  if Choice == 1:
    from main import MainMenu
    MainMenu()
  else:
    return

def loadMenu():
  loadList = []
  i = 1
  for save in [s1, s2, s3]:
    if save.exists() == "True": loadList.append(str(i) + ". Saved")
    else: loadList.append(str(i) + ". Empty")
    i += 1
  loadList.append("Exit")

  loadChoice = selection("Available slots:", loadList, 1)

  confirm = selection("Are you sure you want to load this file?", ["Yes", "No."], 1)
  if confirm == 2: return

  match loadChoice:
    case 1: loadSave(s1)
    case 2: loadSave(s2)
    case 3: loadSave(s3)
    case _: return

def saveMenu():
  saveList = []
  i = 1
  for save in [s1, s2, s3]:
    if save.exists() == "True": saveList.append(str(i) + ". Saved")
    else: saveList.append(str(i) + ". Empty")
    i += 1
  saveList.append("Exit")

  saveChoice = selection("Available save slots:", saveList, 1, 1)
  match saveChoice:
    case 1:
      saveFile(s1)
      updateSaveInfo("True", s2.exists(), s3.exists())
    case 2:
      saveFile(s2)
      updateSaveInfo(s1.exists(), "True", s3.exists())
    case 3:
      saveFile(s3)
      updateSaveInfo(s1.exists(), s2.exists(), "True") 
    case "delete: 2": deleteSave(s2)
    case "delete: 3": deleteSave(s3)
  saveMenu()

def deleteSave(save):
  if save.exists() == "False":
    typingPrint("File is empty.")
    sleep(1)
    return
  else:
    confirm = selection("Are you sure you want to delete this save?", ["Yes", "No"], 1)
    if confirm == 1:
      with open(save.filename, "w") as f: f.write(f" - - - - - - - - Stats - - - - - - - - \n// Health\n\n// Endurance\n\n// Strength\n\n// Agility\n\n// Intelligence\n\n// Luck\n\n// Confidence\n\n// Charisma\n\n// Carry Weight\n\n\n - - - - - - - - Extra - - - - - - - - \n//Past Info\n\n\n - - - - - - Location - - - - - - \n// Location\n\n")
      typingPrint("File deleted.")
      sleep(1)
      if save.name == "s1": updateSaveInfo("False", s2.exists(), s3.exists())
      elif save.name == "s2": updateSaveInfo(s1.exists(), "False", s3.exists())
      elif save.name == "s3": updateSaveInfo(s1.exists(), s2.exists(), "False")
    return

def updateSaveInfo(data1, data2, data3):
  with open("saveInfo.txt", "w") as f: f.write(f" - - - - - Data - - - - - \n// Save 1\n{data1}\n\n// Save 2\n{data2}\n\n// Save 3\n{data3}\n")

def saveFile(save):
  if save.exists() == "True":
    Choice = selection("Are you sure you want to overwrite this file?", ["Yes.", "No."], 1)
    if Choice == 1: pass
    else: saveMenu()
  with open(save.filename, 'w') as f: f.write(f" - - - - - - - - Stats - - - - - - - - \n// Health\n{health}\n// Endurance\n{endurance}\n// Strength\n{strength}\n// Agility\n{agility}\n// Intelligence\n{intelligence}\n// Luck\n{luck}\n// Confidence\n{confidence}\n// Charisma\n{charisma}\n// Carry Weight\n{carryweight}\n\n - - - - - - - - Extra - - - - - - - - \n//Past Info\n{hasPastInfo}\n\n - - - - - - Location - - - - - - \n// Location\n{location}\n")
  return

def loadSave(save):
  global health, endurance, strength, agility, intelligence, luck, confidence, charisma, carryweight, hasPastInfo, location
  hasPastInfo = lc.getline(save.filename, 23)
  health = lc.getline(save.filename, 3)
  endurance = lc.getline(save.filename, 5)
  strength = lc.getline(save.filename, 7)
  agility = lc.getline(save.filename, 9)
  intelligence = lc.getline(save.filename, 11)
  luck = lc.getline(save.filename, 13)
  confidence = lc.getline(save.filename, 15)
  charisma = lc.getline(save.filename, 17)
  carryweight = lc.getline(save.filename, 19)
  location = lc.getline(save.filename, 27)
  import Game
  command = "Game." + location
  exec(command)

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)
