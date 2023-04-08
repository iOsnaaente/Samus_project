from Model.base_model import BaseScreenModel

from kivy.clock import Clock

from Model.db.database import Database 

import socket
# SERVER = '160.238.145.93'
SERVER = '127.0.0.1'
LOGIN_PORT = 50505


class LoginModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.login_screen.LoginScreen.LoginScreenView` class.
    """
    __login_client : socket.socket
    __debug = True 

    __checkbox = 'normal'
    __user = ''
    __psd = ''

    db = Database()

    # sistema de login não usa nenhum tipo de criptografia de dados
    # usar um arquivo xml para isso e colocar cripto em cima 
    def login( self, user, psd ):
        MSG = ('LGN;' + user + ';' + psd + ';').encode()
        try:
            self.__login_client.send( MSG ) 
            ans = self.__login_client.recv( 1024 ).decode()
        except socket.error as e:
            ans = e 
        if self.__debug: 
            print( 'Socket connection OK')
            print( 'Send ', MSG, type(MSG) )
            print( 'Received ', ans, type(ans))
        if ans == '-1' or type(ans) == socket.error :
            return False 
        else:
            return True 

    # Criar novo usuário 
    def create_new_user( self, user, password, family  ):
        if user and password:
            data = 'NEW;' + user + ';' + password + ';' + family
            try: 
                self.__login_client.send( data.encode() )  
                return self.__login_client.recv( 1024 )
            except:
                return False 
        else: 
            return False
    
    # Conectar ao servidor 
    def connect_server( self ):
        try:
            self.__login_client = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
            self.__login_client.connect( (SERVER, LOGIN_PORT) )
            self.__login_client.settimeout( 1 )
            return True 
        except socket.error as e :
            if self.__debug:   print( e )
            Clock.schedule_once( self.connect_server, 1 )
            return False
    

    # Getter and Setter DB properties  
    def get_table(self):
        return self.db.get_login_table()[0]
    def set_table(self, state, user, psd ):
        self.db.set_login_table( state, user, psd )

    # Getter and Setter checkbox property 
    @property 
    def checkbox_keep_login_data( self ): 
        table = self.get_table()
        self.__checkbox = table[1].lower()
        if self.__checkbox == 'down':
            self.__user = table[2]
            self.__psd = table[3]
        return self.__checkbox
    @checkbox_keep_login_data.setter 
    def checkbox_keep_login_data( self, state ):
        self.__checkbox = state  

    # User ans Password model.getters 
    @property
    def user( self ):
        return self.__user 
    @property
    def psd( self ):
        return self.__psd 