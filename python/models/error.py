class EmailError(Exception):
    pass


def email_error():
    raise EmailError('Erro')
