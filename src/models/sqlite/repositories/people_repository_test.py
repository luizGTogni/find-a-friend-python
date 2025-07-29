from pytest import raises
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .people_repository import PeopleRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionError:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_no_result_found
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    repo.insert_person("peopleFirstName", "peopleLastName", 24, 2)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    parameters = mock_connection.session.add.call_args
    person_added = parameters[0][0]

    assert person_added.first_name == "peopleFirstName"
    assert person_added.last_name == "peopleLastName"
    assert person_added.age == 24
    assert person_added.pet_id == 2

def test_insert_person_error():
    mock_connection = MockConnectionError()
    repo = PeopleRepository(mock_connection)

    with raises(Exception):
        repo.insert_person("peopleFirstName", "peopleLastName", 24, 2)

    mock_connection.session.rollback.assert_called_once()
