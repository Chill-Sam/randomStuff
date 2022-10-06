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


 - - - - - - - - Extra - - - - - - - - 
// Past Info


 - - - - - - Location - - - - - - 
// Location


"""



class saves():
    def __init__(self, save_filename):
        self.save_filename = save_filename
        self.is_used = check_is_used(self)

    
    def check_is_used(self):
        line_data = lc.getline(self.savefileName, 1).rstrip()
        is_used = True if line_data == "True" else False
        return is_used


    def delete_save(self):
        with open(self.save_filename, 'w') as savefile:
            savefile.write(EMPTY_DATA)


    def create_save(self)
        with open(self.savefileName, 'w') as savefile:
            savefile.write(f"""
True
 - - - - - - - - Stats - - - - - - - - 
// Health
{health}
// Endurance
{endurance}
// Strength
{strength}
// Agility
{agility}
// Intelligence
{intelligence}
// Luck
{luck}
// Confidence
{confidence}
// Charisma
{charisma}
// Carry Weight
{carry_weight}

 - - - - - - - - Extra - - - - - - - - 
// Past Info
{has_past_info}

 - - - - - - Location - - - - - - 
// Location
{location}

"""
)
