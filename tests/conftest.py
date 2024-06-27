import pytest
from app import create_app

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
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory"
    return app


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def db_session(app):
    from app.extensions import db

    yield db.session
    db.drop_all()
    db.session.close()

