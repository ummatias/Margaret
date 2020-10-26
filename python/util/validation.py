# -*- coding: utf-8 -*-
import re

def email_validation(email):
    if isinstance(email, str):
        regex = r'^[a-z]+[\._]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'

        if re.search(regex, email) != None:
            return email

    raise AttributeError('Email inválido!')

def empty_validation(value, atributo):
    if value == "":
        raise AttributeError(atributo + " não pode ser vazio!") 

def discord_id_validation(value):
    if "#" in value:
        numbers = value.split("#")
        regexNumbers = r'^[0-9]{4}$'

        if  re.search(regexNumbers,numbers[1]) != None:
            return value
        
    raise AttributeError ("Discord inválido!")