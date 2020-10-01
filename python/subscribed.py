from python.user import User


class Subscribed(User):
    def __init__(self, name, email, discord_id, period='', minority_group=''):
        User.__init__(self, name, email, discord_id)
        self.__period = period
        self.__minority_group = minority_group

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, value):
        return self.__period


# Examples


s1 = Subscribed('Fernando Guimarães', 'fernando.guimaraes@ccc.ufcg.com', '8955888899', '2020.1', 'negros')

print(s1.__dict__)

print(s1.period)
