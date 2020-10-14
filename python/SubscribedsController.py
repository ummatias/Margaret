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
        return list(self.subscribeds.values())

    def find_subscribed_by_attribute(self,attribute,value):
        if attribute.lower() not in['name','email','discord','period','minoritary_group']:
            raise AttributeError("Atributo inválido")

        found_subscribeds = {}
        
        for key, val in enumerate(self.subscribeds.values()):
           if value.lower() in getattr(val,attribute):
               found_subscribeds.update({key,val})
        
        return found_subscribeds


    def modify_subscribed_by_attribute(self,email_user,attribute,new_attribute):
        if attribute.lower() not in['name','email','discord','period','minoritary_group']:
            raise AttributeError("Atributo inválido")
        
        self.validate_subscribed_existence(email_user)
        
        if attribute == 'email':
            self.email_validacion(email_user)
        
            
    def remove_subscribed(self,email_user):
        self.validate_subscribed_existence(email_user)
        del self.subscribeds[email_user]

    def validate_subscribed_existence(self,email_user):
        if not email_user in self.subscribeds.keys():
            raise Exception("Usuário não inscrito")

    def email_validacion(self,email):
        regex = '^[a-z]+[./_]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'
        try:
            if re.search(regex,email):
                email_error()
        except EmailError as error:
            print(error)

    def validating_existing_email(self,email):
        for subs in self.subscribeds:
            if subs.email == email:
                raise Exception("Email já em uso")
            
    
    