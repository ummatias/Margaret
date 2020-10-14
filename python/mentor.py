from user import User


class Mentor(User):
    def __init__(self, name, email, discord_id, state='',organization=''):
        User.__init__(self, name, email, discord_id)
        self.__state = state
        self.__organization = organization

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self,value):
        self.__organization = value
