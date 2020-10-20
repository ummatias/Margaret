# -*- coding: utf-8 -*-

from project import Project


class ProjectController:
    def __init__(self):
        self.projects = dict()
        self.current_id = 0

    def add_project(self, name, description, base_text, mentor, mentor_aux, areas):
        project_id = 1
        for _ in self.projects:
            project_id += 1
        self.current_id = project_id

        project = Project(name, description, base_text, project_id, mentor, mentor_aux, areas).__dict__
        self.projects[project_id] = project
        return project_id

    def list_projects(self):
        return list(self.projects.values())

    def find_projects_by_state(self, state):
        found_projects = {}

        for key, val in enumerate(self.projects.values()):
            if val.get('state') == state:
                found_projects.update({key + 1: val})
        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def find_projects_by_area(self, areas):
        found_projects = {}

        for key, val in enumerate(self.projects.values()):
            if val.get('areas') == areas:
                found_projects.update({key: val})
        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def update_project_name(self, counter_id, new_name):
        for i, val in enumerate(self.projects.values()):
            if (counter_id - 1) == i:
                val['name'] = new_name
                return val
            elif counter_id not in self.projects:
                raise Exception('Index Error')

    def update_project_description(self, counter_id, new_description):
        for i, val in enumerate(self.projects.values()):
            if (counter_id - 1) == i:
                val['description'] = new_description
                return val
            elif counter_id not in self.projects:
                raise Exception('Index Error')


