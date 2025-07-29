from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.people import PeopleTable
from .people_repository import PeopleRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    repo.insert_person("peopleFirstName", "peopleLastName", 24, 2)
    person_data = PeopleTable(
        first_name="peopleFirstName",
        last_name="peopleLastName",
        age=24,
        pet_id=2
    )

    mock_connection.session.add.assert_called_once_with(person_data)


def test_insert_person_error():
    pass

def test_get_person():
    pass

def test_get_person_no_result():
    pass
