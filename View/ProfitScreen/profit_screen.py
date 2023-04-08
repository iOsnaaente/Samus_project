from View.base_screen import BaseScreenView
from View.base_screen import SwipeScreen 

from kivy.lang import Builder 
import os 
PATH = os.path.dirname( __file__ )
Builder.load_file( PATH + '/profit_screen.kv')

class ProfitScreenView( BaseScreenView, SwipeScreen ):

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
