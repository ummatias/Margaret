#coding: utf-8
class Project:
    def __init__(self, name, description, base_text, project_id, mentor, aux_mentor, areas):
        self.name = name
        self.description = description
        self.base_text = base_text
        self.project_id = project_id
        self.mentor = mentor
        self.aux_mentor = aux_mentor
        self.areas = areas
        self.state = "Em análise"
        self.subscribers = {}
