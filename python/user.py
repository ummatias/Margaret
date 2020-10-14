# -*- coding: utf-8 -*-

import re


class User:
    def __init__(self, name='', email='', discord_id=''):
        self.name = name
        self.email = email
        self.discord_id = discord_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            value = value.upper()
            self._name = value
        else:
            raise Exception('Invalid name!')

    def email_validacion(self):
        regex = '^[a-z]+[\._]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'

        if re.search(regex, self.email):
            return self.email
        else:
            raise Exception('Invalid mail!')
            
