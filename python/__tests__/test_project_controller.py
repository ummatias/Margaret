from python.project_controller import ProjectController


def test_id_validation():
    collections = ProjectController()

    collections.add_project('Laguinho', '', '', '', '', '')
    assert collections.current_id == 1

    collections.add_project('Margaret', '', '', '', '', '')
    assert collections.current_id == 2


def test_find_state():
    collections = ProjectController()

    collections.add_project('Roadmap', '', '', '', '', '')
    project = collections.projects[1]

    assert project.get('state') == 'Em análise'


def test_find_area():
    collections = ProjectController()

    collections.add_project('Tamburetei', '', '', '', '', 'Web')
    project = collections.projects[1]

    assert project.get('areas') == 'Web'


def test_update_project_name():
    collections = ProjectController()

    collections.add_project('Horários', '', '', '', '', 'Web')

    collections.update_project_name(1, 'IssueAi')
    project = collections.projects[1]

    assert project.get('name') == 'IssueAi'


def test_update_project_description():
    collections = ProjectController()
    collections.add_project('Glossário', 'Sem descrição', '', '', '', 'Web')

    collections.update_project_description(1, 'Com descrição')
    project = collections.projects[1]

    assert project.get('description') == 'Com descrição'
