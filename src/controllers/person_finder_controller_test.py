#pylint: disable=unused-argument
from pytest import raises
from src.models.sqlite.entities.people import PeopleTable
from .person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPeopleRepository:
    def get_person(self, person_id: int) -> PeopleTable:
        return MockPerson(
            first_name="John",
            last_name="Doe",
            pet_name="Fluffy",
            pet_type="cat"
        )

class MockPeopleRepositoryNotFound:
    def get_person(self, person_id: int) -> PeopleTable:
        return None

def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(20)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"]["first_name"] == "John"
    assert response["data"]["attributes"]["last_name"] == "Doe"
    assert response["data"]["attributes"]["pet_name"] == "Fluffy"
    assert response["data"]["attributes"]["pet_type"] == "cat"

def test_find_error_not_found():
    controller = PersonFinderController(MockPeopleRepositoryNotFound())

    with raises(Exception):
        controller.find(200)
