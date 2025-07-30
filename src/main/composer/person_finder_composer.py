from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_finder_controller import PersonFinderController
from src.views.person_finder_view import PersonFinderView

def person_finder_composer():
    repository = PeopleRepository(db_connection_handler)
    controller = PersonFinderController(repository)
    view = PersonFinderView(controller)

    return view
