import linecache as lc


EMPTY_DATA = """
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


 - - - - - - Location - - - - - - 
// Location


""".lstrip()



class saves():
    def __init__(self, save_filename, player):
        self.save_filename = save_filename
        self.is_used = self.check_is_used()
        self.player = player

    
    def check_is_used(self):
        line_data = lc.getline(self.save_filename, 1).rstrip()
        is_used = True if line_data == "True" else False
        return is_used


    def delete_save(self):
        with open(self.save_filename, 'w') as savefile:
            savefile.write(EMPTY_DATA)


    def create_save(self):
        with open(self.save_filename, 'w') as savefile:
            savefile.write(
f"""
True
 - - - - - - - - Stats - - - - - - - - 
// Health
{self.player.health}
// Endurance
{self.player.endurance}
// Strength
{self.player.strength}
// Agility
{self.player.agility}
// Intelligence
{self.player.intelligence}
// Luck
{self.player.luck}
// Confidence
{self.player.confidence}
// Charisma
{self.player.charisma}
// Carry Weight
{self.player.carry_weight} 

 - - - - - - Location - - - - - - 
// Location
{self.player.location}
""".lstrip()
)

    def load_save(self):
        self.player.health = lc.getline(self.save_filename, 4).rstrip()
        self.player.endurance = lc.getline(self.save_filename, 6).rstrip()
        self.player.strength = lc.getline(self.save_filename, 8).rstrip()
        self.player.agility = lc.getline(self.save_filename, 10).rstrip()
        self.player.intelligence = lc.getline(self.save_filename, 12).rstrip()
        self.player.luck = lc.getline(self.save_filename, 14).rstrip()
        self.player.confidence = lc.getline(self.save_filename, 16).rstrip()
        self.player.charisma = lc.getline(self.save_filename, 18).rstrip()
        self.player.carry_weight = lc.getline(self.save_filename, 20).rstrip()
        self.player.location = lc.getline(self.save_filename, 24).rstrip()