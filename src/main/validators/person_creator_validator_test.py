from .person_creator_validator import person_creator_validator

class MockRequest:
    def __init__(self, body):
        self.body = body

def test_person_creator_validator_test():
    request = MockRequest({
        "first_name": "John",
        "last_name": "Doe",
        "age": 24,
        "pet_id": 5
    })

    person_creator_validator(request)
