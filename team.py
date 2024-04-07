#Import the date time module to work with dates and time.
import datetime

#Create a class named Team to keep information about the teams participating
class Team:
    id_counter = 0  # Class-level variable to keep track of IDs
    
    def __init__(self, name, team_type, fee_paid, fee_amount,date_created=None, cancellation_date = None):
        Team.id_counter += 1
        self.__id = Team.id_counter  # Assign the next available ID 
        if date_created is None:
            self.__date_created = datetime.datetime.now()
        else:
            self.__date_created = date_created
        self.__name = name
        self.__team_type = team_type
        self.__fee_paid = fee_paid
        self.__fee_amount = fee_amount
        self.__cancellation_date = cancellation_date
    
    #Creating get and set methods for all instances     
    def get_id(self):
        return self.__id
    
    def get_date_created(self):
        return self.__date_created               
            
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
           
    def set_team_type(self, team_type):
        self.__team_type = team_type
    
    def get_team_type(self):
        return self.__team_type
    
    def set_fee_paid(self, fee_paid):
        self.__fee_paid = fee_paid
    
    def get_fee_paid(self):
        return self.__fee_paid
    
    def set_fee_amount(self, fee_amount):
        self.__fee_amount = fee_amount
        
    def get_fee_amount(self):
        return self.__fee_amount
    
    def get_cancellation_date(self):
        return self.__cancellation_date
    
    def set_cancellation_date(self, cancellation_date):
        self.__cancellation_date = cancellation_date