import pytest


@pytest.fixture(scope='function')
def db():
    print('*****SETUP DB*****')
    yield db
    print('******TEARDOWN DB******')


@pytest.fixture(scope='function')
def source():
    print('*****SETUP SOURCE*****')
    yield source
    print('******TEARDOWN SOURCE******')


def test_fixture_request(db, source, request):
    print('Test the request fixture')  # Set breakpoint here to inspect request instance
