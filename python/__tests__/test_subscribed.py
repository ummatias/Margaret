from python.models.user import User
from python.models.subscribed import Subscribed
from pytest import fail

def test_subscribed_create_sucess():
    sub = Subscribed('Midorya', 'deku.arumairo@ccc.ufcg.edu.br', 'Deku#1969', '1', 'LGBTQA+')

    assert sub.name == 'MIDORYA'
    assert sub.email == 'deku.arumairo@ccc.ufcg.edu.br'
    assert sub.discord_id == 'Deku#1969'
    assert sub.period == '1'
    assert sub.minority_group == 'LGBTQA+'

def test_subscribed_null_fields():
    try:
        sub = Subscribed(None,None,None,None)
        fail()
    except AttributeError:
        pass

def test_subscribed_empty_name():
    try:
        sub = Subscribed('', 'lida.runner@ccc.ufcg.edu.br', 'Lida#5674', '1', '')
        fail()
    except AttributeError:
        pass

def test_subscribed_empty_email():
    try:
        sub = Subscribed('Tsuyu', '', 'Tsuyu#5674', '1', '')
        fail()
    except AttributeError:
        pass

def test_subscribed_empty_discord():
    try:
        sub = Subscribed('Mineta', 'mineta.bubble@ccc.ufcg.edu.br', '', '1', '')
        fail()
    except AttributeError:
        pass

def test_subscribed_name_not_string():
    try:
        sub = Subscribed(7845, 'uraraka.fly@ccc.ufcg.edu.br', 'Gravity#4842', '1')
        fail()
    except AttributeError:
        pass

def test_subcribed_email_format_wrong():
    try:
        sub = Subscribed('Todoroki', 'todoroki.shoto@3232.com.xr' 'Shoto#8475', '1')
        fail()
    except AttributeError:
        pass

def test_subscribed_negative_period():
    try:
        sub = Subscribed('Bakugo', 'bakugo.numberone@ccc.ufcg.edu.br', 'Boom#4576', '-1')
        fail()
    except AttributeError:
        pass
