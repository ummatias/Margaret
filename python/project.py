class Project:
	def __init__(self, name, description, base_text, project_id, mentor, aux_mentor, areas, state, subscribeds):
		self.name = name
		self.description = description
		self.base_text = base_text
		self.project_id = project_id
		self.mentor = mentor
		self.aux_mentor = aux_mentor
		self.areas = areas
		self.state = "Em análise"
		self.subscribeds = {}

	@property
	def name(self):
		return self.name
	
	@name.setter
	def name(self, name):
		self.name = name

	@property
	def description(self):
		return self.description
		
	@description.setter
	def description(self, description):
		self.description = description
	
	@property
	def base_text(self):
		return self.base_text
		
	@description.setter
	def base_text(self, base_text):
		self.base_text = base_text
	
	@property
	def project_id(self):
		return self.project_id
		
	@description.setter
	def project_id(self, project_id):
		self.project_id = project_id
	
	@property
	def mentor(self):
		return self.mentor
		
	@description.setter
	def mentor(self, mentor):
		self.mentor = mentor
	
	@property
	def aux_mentor(self):
		return self.aux_mentor
		
	@description.setter
	def aux_mentor(self, aux_mentor):
		self.aux_mentor = aux_mentor
	
	@property
	def areas(self):
		return self.areas
		
	@description.setter
	def areas(self, areas):
		self.areas = areas
	
	@property
	def state(self):
		return self.state
		
	@description.setter
	def state(self, state):
		self.state = state
	
	@property
	def subscribeds(self):
		return self.subscribeds
		
	def add_subscribeds(self, key, value):
		self.subscribeds[key] = value
	
	def get_subscribeds(self, key):
		return self.subscribeds[key]
