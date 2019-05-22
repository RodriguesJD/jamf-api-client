from oop_jamf.departments import Departments

item = Departments().get_trr_jamf()


def test_departments():

    assert item.status_code == 200


def test_departments_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Departments().by_name(test_name).status_code == 200


def test_departments_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Departments().by_id(test_id).status_code == 200

