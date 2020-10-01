from python.user import User


class Mentor(User):
    def __init__(self, name, email, discord_id, state=''):
        User.__init__(self, name, email, discord_id)
        self.__state = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value


# Examples


m1 = Mentor('carlos siqueira', 'carlos@gmail.com', 'carlos#8999', 'homologado')

print(m1.__dict__)

print(m1.state)

print(m1.name)