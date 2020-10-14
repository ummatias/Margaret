from subscribed import Subscribed
from error import *
import re

class SubscribedsController:

    def __init__(self):
        self.subscribeds = {}       

    def add_subscribed(self,name,email,discord,period,minoritary_group):
        self.validating_existing_email(email)
        subscribed = Subscribed(name,email,discord,period,minoritary_group)       
        self.subscribeds[email] = subscribed
        return self.subscribeds[email]

    def list_subscribeds(self):
        return self.subscribeds.values()

    def find_subscribed_by_attribute(self,attribute,value_attribute):
        if attribute.lower() not in['name','email','discord','period','minoritary_group']:
            raise AttributeError("Atributo inválido")

        found_subscribeds = []
        
        for sub in self.subscribeds.values():
           if value_attribute.lower() in getattr(sub,attribute):
               found_subscribeds.append(sub)
        
        return found_subscribeds


    def modify_subscribed_by_attribute(self,email_user,attribute,new_attribute):
        if attribute.lower() not in['name','email','discord','period','minoritary_group']:
            raise AttributeError("Atributo inválido")
        
        self.validate_subscribed_existence(email_user)
        
        if attribute == 'email':
            self.email_validation(new_attribute)

        setattr(self.subscribeds[email_user],attribute,new_attribute)
        
            
    def remove_subscribed(self,email_user):
        self.validate_subscribed_existence(email_user)
        del self.subscribeds[email_user]

    def validate_subscribed_existence(self,email_user):
        if not email_user in self.subscribeds.keys():
            raise ValueError("Usuário não inscrito")

    def email_validation(self,email):
        regex = '^[a-z]+[./_]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'
        try:
            if re.search(regex,email):
                email_error()        
        except:
            raise EmailError("Email inválido")

    def validating_existing_email(self,email):
        if email in self.subscribeds.keys():
            raise ValueError("Email já em uso")    
    
    