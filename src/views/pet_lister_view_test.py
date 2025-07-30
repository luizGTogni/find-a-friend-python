from typing import Dict
from src.views.http_types.http_request import HttpRequest
from .pet_lister_view import PetListerView

class MockPetListerController:
    def list(self) -> Dict:
        return {
            "data": {
                "type": "Pets",
                "count": 2,
                "attributes": [
                    { "name": "Fluffy", "type": "Cat", "id": 1 },
                    { "name": "Bob", "type": "Dog", "id": 2 },
                ]
            }
        }

def test_pet_lister_view():
    view = PetListerView(MockPetListerController())
    response = view.handle(HttpRequest())

    assert response.status_code == 200
    assert response.body == {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "Fluffy", "type": "Cat", "id": 1 },
                { "name": "Bob", "type": "Dog", "id": 2 },
            ],
        }
    }
