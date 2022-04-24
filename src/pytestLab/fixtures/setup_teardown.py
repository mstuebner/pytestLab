import pytest


@pytest.fixture()
def db():
    """
    This could be a fixture that established a database connection before test and takes it down after
    """
    print('*****SETUP DB*****')
    # Any creation or establishment to prepare the fixture is done here, before "yield" is called...
    yield db  # This is where the fixture returns to the test
    # ...and everything to clean up follows at this point
    print('******TEARDOWN DB******')


@pytest.fixture(scope='function')  # scope='function' is default, so doesn't change anything
def source():
    print('*****SETUP SOURCE*****')
    yield source
    print('******TEARDOWN SOURCE******')


def test_test1(db, source):
    print('Test1: "db" is setup and taken down BEFORE "source')


def test_test2(source, db):
    print('Test1: "db" is setup and taken down AFTER "source')
