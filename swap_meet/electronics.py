#______________________WAVE 5___________________________________
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = None, age = None):
        super().__init__("Electronics", condition, age)
        
        
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    
 