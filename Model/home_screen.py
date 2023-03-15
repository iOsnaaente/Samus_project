from Model.base_model import BaseScreenModel

import os 

PATH = os.path.dirname( __file__ ).removesuffix( '\\Model' )

class HomeScreenModel(BaseScreenModel):
    
    photo_image = PATH + '/images/bruno-sampaio.jpg'
    username = 'Bruno Sampaio'
    renda_total = 'R$ ' + str(11900)

    """
    Implements the logic of the
    :class:`~View.home_screen.HomeScreen.HomeScreenView` class.
    """