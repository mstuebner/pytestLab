import pytest
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('tests')

# @pytest.fixture(scope='module')
@pytest.fixture()
def db():
    print('*****SETUP DB*****')
    yield db
    print('******TEARDOWN DB******')


# @pytest.fixture(scope='function')
@pytest.fixture()
def source():
    print('*****SETUP SOURCE*****')
    yield db
    print('******TEARDOWN SOURCE******')


def test_scott_data(db, source, request, caplog):
    caplog.set_level(logging.INFO)
    log.info('info log')
    log.warning('warning log')
    log.error('error log')
    log.exception('exception log')
    print('scott data')


def test_mark_data(source, db, request, caplog):
    print('mark data')
