import pytest
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('buildin_fixture_caplog')


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


def test_fixture_caplog_default(db, source, caplog):
    log.info('This log will not show up in caplog')
    log.warning('warning log')
    print('test_fixture_caplog_default')  # Set breakpoint here to inspect caplog instance


def test_fixture_caplog_setlevel(db, source, caplog):
    caplog.set_level(logging.INFO)
    log.info('Now also this INFO log will not show up in caplog')
    log.warning('warning log')
    print('test_fixture_caplog_setlevel')  # Set breakpoint here to inspect caplog instance
