class Organization:

    def __init__(self, name, desc, owner, category, org_id):
        self._name = name
        self._desc = desc
        self._owner = owner
        self._category= category
        self._org_id = org_id
        self._state = "Em análise"
        self._projects = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        self._desc = desc


    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner

    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    
    @property
    def org_id(self):
        return self._org_id

    @property
    def projects(self):
        return self._projects

    def project_add(self, key, value):
        self._projects[key] = [value]

    def project_get(self, key):
        return self._projects[key]

