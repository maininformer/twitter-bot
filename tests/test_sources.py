import os
import pytest

from from_root import from_root

from src.sources.file import Source

@pytest.fixture(scope='module')
def source():
    TEST_INPUT_LOG_ADDRESS = from_root('tests') / 'test_input_log'
    with open(f'{TEST_INPUT_LOG_ADDRESS}', 'w') as f:
        f.writelines(['ctrlp is cool\n', 'vim is cool\n', 'nerdtree is cool\n'], )
    yield Source(TEST_INPUT_LOG_ADDRESS)
    os.remove(TEST_INPUT_LOG_ADDRESS)
    os.remove(from_root('tests') / 'test_input_log_handleds')

def test_create_a_handleds_log(source):
    assert source.handleds_log == []

def test_handle_first_entry(source):
    assert source.next() == 'ctrlp is cool'

def test_update_handled(source):
    source.update_handleds(source.next())
    assert source.handleds_log == ['ctrlp is cool']

def test_handle_second_entry(source):
    assert source.next() == 'vim is cool'
    source.update_handleds(source.next())
    assert source.handleds_log == ['ctrlp is cool', 'vim is cool']

def test_handle_last_entry(source):
    assert source.next() == 'nerdtree is cool'
    source.update_handleds(source.next())
    assert source.handleds_log == ['ctrlp is cool', 'vim is cool', 'nerdtree is cool']

def test_does_not_fail_when_all_caught_up(source):
    assert source.next() == ''

def test_commit(source):
    source.commit()
    with open(source.handleds_address, 'r') as f:
            assert [x.strip('\n') for x in f.readlines()] == ['ctrlp is cool', 'vim is cool', 'nerdtree is cool']






