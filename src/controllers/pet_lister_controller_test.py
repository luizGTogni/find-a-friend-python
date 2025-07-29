from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=1, name="Dog", type="Dog"),
            PetsTable(id=2, name="Cat", type="Cat")
        ]

class MockPetsRepositoryEmptyList:
    def list_pets(self):
        return []

def test_list():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    assert response["data"]["type"] == "Pets"
    assert response["data"]["count"] == 2
    assert response["data"]["attributes"][0]["id"] == 1
    assert response["data"]["attributes"][0]["name"] == "Dog"
    assert response["data"]["attributes"][0]["type"] == "Dog"

def test_list_empty():
    controller = PetListerController(MockPetsRepositoryEmptyList())
    response = controller.list()

    assert response["data"]["type"] == "Pets"
    assert response["data"]["count"] == 0
    assert not response["data"]["attributes"]
