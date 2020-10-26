# -*- coding: utf-8 -*-
import re

def email_validation(email):
    if isinstance(email, str):
        regex = '^[a-z]+[\._]?[a-z]+[@]{1}[c]{3}[.][c-u]{4}[.][d-u]{3}[.][b-r]{2}$'

        if re.search(regex, email) != None:
            return email

    raise AttributeError('Email inválido!')

def period_validation(period):
    if period != '':
        if int(period) < 0:
            raise AttributeError('Período inválido!')
    else:
        return period

def empty_validation(value, atributo):
    if value == "":
        raise AttributeError(atributo + " não pode ser vazio!")