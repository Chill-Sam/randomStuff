import linecache as lc

EMPTYDATA = """
False
 - - - - - - - - Stats - - - - - - - - 
// Health

// Endurance

// Strength

// Agility

// Intelligence

// Luck

// Confidence

// Charisma

// Carry Weight


 - - - - - - - - Extra - - - - - - - - 
// Past Info


 - - - - - - Location - - - - - - 
// Location


"""



class saves():
    def __init__(self, savefileName):
        self.savefileName = savefileName
        self.isUsed = checkIsUsed(self)

    
    def checkIsUsed(self):
        lineData = lc.getline(self.savefileName, 1).rstrip()
        isUsed = True if lineData == "True" else False
        return isUsed


    def deleteSave(self):
        with open(self.savefileName, 'r') as savefile:
            savefile.write(EMPTYDATA)


    def createSave(self)
        with open(self.savefileName, 'r') as savefileIN and open(self.savefileName, 'w') as savefileOUT:
            lines = savefileIN.readlines()
            lines[0] = "True\n"
            savefileOUT.write(lines)



def displaySaves():
    pass

def selectSave():
    pass

def save():
    pass
    


