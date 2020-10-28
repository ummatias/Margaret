# -*- coding: utf-8 -*-

from python.models.user import User


class Subscribed(User):
    def __init__(self, name, email, discord_id, period='', minority_group=''):
        User.__init__(self, name, email, discord_id)
        self.period = period
        self.minority_group = minority_group

