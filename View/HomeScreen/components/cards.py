from kivy.properties import NumericProperty 
from kivy.properties import StringProperty  
from kivy.properties import ColorProperty 
from kivymd.uix.card import MDCard 

class MDCardValue( MDCard ):
    icon             = StringProperty()   
    type             = StringProperty()   
    used_value       = StringProperty()       
    to_use_value     = StringProperty()           
    available_value  = StringProperty()           
    progress_value   = NumericProperty()          
    color_available  = ColorProperty()     

    def __init__(self, icon, type, used_value, to_use_value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.icon = icon                   
        self.type = type                   
        self.used_value = 'R$' + str( used_value)              
        self.to_use_value = 'R$' + str( to_use_value )   
        available_value =  to_use_value - used_value
        if available_value > 0:     self.color_available = [119/255, 221/255, 119/255, 0.95 ]
        elif available_value < 0:   self.color_available = [196/255, 2/255  , 51/255 , 0.95 ]
        else:                       self.color_available = [255/255, 247/255, 85/255 , 0.95 ]
        self.available_value = 'R$' + str( available_value )
        self.progress_value = round(used_value/to_use_value*100, 3)
