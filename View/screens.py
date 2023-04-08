# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.home import HomeModel
from Model.login import LoginModel

from Controller.login_screen import LoginController

from Controller.profit_screen import ProfitController
from Controller.home_screen import HomeController
from Controller.extrato_screen import ExtratoController

screens = {
    'login screen': {
        'model': LoginModel,
        'controller': LoginController,
    },
    'profit screen': {
        'model': HomeModel,
        'controller': ProfitController,
    },
    'home screen': {
        'model': HomeModel,
        'controller': HomeController,
    },
    'extrato screen': {
        'model': HomeModel,
        'controller': ExtratoController,
    }
}