import pytest
from app import create_app
from app.models import db

"""
Fixture scopes: A little reminder

Fixtures are created when first requested by a test, and are destroyed based on their scope:
    function: the default scope, the fixture is destroyed at the end of the test.
    class: the fixture is destroyed during teardown of the last test in the class.
    module: the fixture is destroyed during teardown of the last test in the module.
    package: the fixture is destroyed during teardown of the last test in the package.
    session: the fixture is destroyed at the end of the test session.
"""


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory"
    return app


@pytest.fixture(scope="function")
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()
