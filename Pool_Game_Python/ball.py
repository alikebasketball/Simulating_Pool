# This is what we will store our ball class in

# Lets do our imports
import math

# Let's create our class
class Ball():
    def __init__(self, a, b) -> None:
        self.x = 5
        self.y = 5
        self.xvel = a
        self.yvel = b
        self.status = 'Moving..'
        
    def locate_ball(self):
        print(f'The ball is located at {self.x},{self.y}..')
    
    def set_status(self):
        if math.sqrt(((self.x - 10)**2) + ((self.y - 10)**2)) <= 1:
            self.status = 'YOU DID IT MATE! HIT!!!'
        
        elif math.sqrt(((self.x - 0)**2) + ((self.y - 0)**2)) <= 2:
            self.status = 'Jeez man.. Did not know you were an amateur..'
        
        else:
            self.status = 'Moving..'
    
    def update(self):
        self.x = self.x + self.xvel * 0.01
        self.y = self.y + self.yvel * 0.01
        
        if self.x < 0 and self.xvel < 0:
            self.xvel = self.xvel * -1
        
        if self.x > 10 and self.xvel > 0:
            self.xvel = self.xvel * -1
            
        if self.y < 0 and self.yvel < 0:
            self.yvel = self.yvel * -1
        
        if self.y > 10 and self.yvel > 0:
            self.yvel = self.yvel * -1
        
        self.set_status()
    
    def reset_status(self):
        self.status = 'Moving..'
        
# number inputs for game
def numinput():
    """Gather user input for the game

    Args:
        u (int): Coordinates
    """
    active = True
    while active:
        u = input('Enter Coordinates: ')
        
        if u.isnumeric() and int(u) > 0:
            return int(u)
        
        
        else:
            print('Nice going.. You died..')
            break
        