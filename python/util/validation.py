# -*- coding: utf-8 -*-
import re

def email_validation(email):
        regex = '^[a-z]+[\._]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'
        try:
            if re.search(regex,email):
                return email        
        except:
            raise Exception("Email inválido")
