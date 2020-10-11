#coding: utf-8
class Organization:

    def __init__(self, name, desc, owner, category, org_id):
        self.name = name
        self.desc = desc
        self.owner = owner
        self._category = category
        self.org_id = org_id
        self._state = "Em análise"
        self.projects = {}

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not (category in ['laboratório', 'organização estudantil', 'externa']):
            raise Exception('Categoria Inválida')
        self._category = category

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if not (state in ['Em análise', 'Necessita Revisão', 'Pronto']):
            raise Exception('Estado Inválido')
        self._state = state


    def add_project(self, key, value):
        self.projects[key] = [value]

    def get_project(self, key):
        return self.projects[key]
