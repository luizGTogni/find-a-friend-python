# pylint: disable=unused-argument
from typing import Dict
from src.views.http_types.http_request import HttpRequest
from .person_finder_view import PersonFinderView

class MockPersonFinderController:
    def find(self, person_id: int) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "pet_name": "Fluffly",
                    "pet_type": "Cat",
                },
            }
        }

def test_person_finder_view():
    view = PersonFinderView(MockPersonFinderController())
    response = view.handle(HttpRequest(param={ "person_id": 1 }))

    print(response.body)

    assert response.status_code == 200
    assert response.body == {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fluffly",
                "pet_type": "Cat",
            },
        }
    }
