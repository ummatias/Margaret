class User:
    #id = 1

    def __init__(self, name='', email='', discord_id=''):
        # self.id = User.id
        self.name = name
        self.__email = email
        self.__discord_id = discord_id
        # User.id += self.id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = value.lower().title()
        self.__name = value

    """
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def discord_id(self):
        return self.__discord_id

    @discord_id.setter
    def discod_id(self, value):
        return self.__discord_id 
    """
