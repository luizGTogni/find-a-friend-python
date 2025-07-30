# pylint: disable=unused-argument
from typing import Dict
from src.views.http_types.http_request import HttpRequest
from .pet_deleter_view import PetDeleterView

class MockPetDeleterController:
    def delete(self, name: str) -> Dict:
        return None

def test_pet_deleter_view():
    view = PetDeleterView(MockPetDeleterController())
    response = view.handle(HttpRequest(param={ "name": "PetName" }))

    assert response.status_code == 204
    assert not response.body
