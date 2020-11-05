# -*- coding: utf-8 -*-

from models.project import Project


class ProjectController:
    def __init__(self):
        self.projects = dict()
        self.current_id = 0

    def add_project(self, name, description, base_text, mentor, mentor_aux, areas):
        project_id = 1
        for _ in self.projects:
            project_id += 1
        self.current_id = project_id

        project = Project(name, description, base_text,
                          project_id, mentor, mentor_aux, areas)
        self.projects[project_id] = project
        return project_id

    def list_projects(self):
        return list(self.projects.values())

    def find_projects_by_state(self, state):
        found_projects = {}

        for key, val in enumerate(self.projects.values()):
            if val.state == state:
                found_projects.update({key + 1: val})

        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def find_projects_by_area(self, area):
        found_projects = {}

        for key, val in enumerate(self.projects.values()):
            if area in val.areas:
                found_projects.update({key + 1: val})

        if not found_projects:
            raise Exception('Projects not found!')

        return found_projects

    def update_project_name(self, current_id, new_name):
        if current_id in self.projects:
            project = self.projects.get(current_id)
            project.name = new_name
            return project
        else:
            raise Exception('Index Error')

    def update_project_description(self, current_id, new_description):
        if current_id in self.projects:
            project = self.projects.get(current_id)
            project.description = new_description
            return project
        else:
            raise Exception('Index Error')

    def update_project_base_text(self, current_id, new_base_text):
        if current_id in self.projects:
            project = self.projects.get(current_id)
            project.base_text = new_base_text
            return project
        else:
            raise Exception('Index Error')

    def add_project_area(self, current_id, new_area):
        if current_id in self.projects:
            project = self.projects[current_id]
            project.areas.append(new_area)
            return project
        else:
            raise Exception('Index Error')

    def remove_project_area(self, current_id, area):
        if current_id in self.projects:
            project = self.projects[current_id]
            try:
                project.areas.remove(area)
                return area
            except ValueError as e:
                return e
        else:
            raise Exception('Index Error')

    def update_project_state(self, current_id, new_state):
        if current_id in self.projects:
            project = self.projects[current_id]
            project.state = new_state
            return new_state
        else:
            raise Exception('Index Error')

    def remove_project(self, current_id):
        if current_id in self.projects:
            del self.projects[current_id]
            return self.projects
        else:
            raise Exception('Index Error')

    def find_project_by_mentor(self, email_mentor):
        for key, project in enumerate(self.projects.values()):
            if project.mentor.email == email_mentor or project.mentor_aux.email == email_mentor:
                return project
            else:
                raise Exception('Project not found!')
