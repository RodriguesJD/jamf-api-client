from oop_jamf.diskencryptionconfigurations import Diskencryptionconfigurations

item = Diskencryptionconfigurations().get_trr_jamf()


def test_diskencryptionconfigurations():

    assert item.status_code == 200


def test_diskencryptionconfigurations_by_name():
    first_key = list(item.json().keys())[0]
    test_name = item.json()[first_key][0]['name']
    assert Diskencryptionconfigurations().by_name(test_name).status_code == 200


def test_diskencryptionconfigurations_by_id():
    first_key = list(item.json().keys())[0]
    test_id = item.json()[first_key][0]['id']
    assert Diskencryptionconfigurations().by_id(test_id).status_code == 200

