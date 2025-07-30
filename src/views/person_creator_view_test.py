from typing import Dict
from .http_types.http_request import HttpRequest
from .person_creator_view import PersonCreatorView

class MockPersonCreatorController:
    def create(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info,
            }
        }

def test_person_creator_view():
    view = PersonCreatorView(MockPersonCreatorController())
    response = view.handle(HttpRequest(
                body={
                    "first_name": "John",
                    "last_name": "Doe",
                    "age": 30,
                    "pet_id": 2,
                }
            )
        )

    assert response.status_code == 201
    assert response.body == {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "age": 30,
                    "pet_id": 2,
                },
            }
        }
