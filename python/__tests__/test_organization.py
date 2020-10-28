#coding: utf-8
from python.models.organization import Organization

def test_category_setter():

    org = Organization("org", "", "", "laboratório", "")

    try:
        org.category = "aleatorio"
        assert False
    except:
        assert True

def test_state_setter():

    org = Organization("org", "", "", "laboratório", "")

    try:
        org.state = "aleatorio"
        assert False
    except:
        assert True

def test_add_project():

    org = Organization("org", "", "", "laboratório", "")

    org.add_project(1, "projeto1")

    assert org.get_project(1) == "projeto1"

    org.add_project(1, "projeto2")

    assert org.get_project(2) == "projeto2"

    org.add_project(2, "projeto3")

    assert org.get_project(3) == "projeto3"