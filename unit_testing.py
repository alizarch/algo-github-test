import pytest
from python_test import parse_data, copy_data, functional_data, random_data, bad_data

def test_parse_data():
    parse_commands = parse_data()
    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]

def test_copy_data():
    copy_commands = copy_data()
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]

def test_functional_data():
    functional_commands  = functional_data()
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]

def test_random_data():
    random_commands = random_data()
    assert len(random_commands) == 2

def test_bad_data():
    bad_commands = bad_data()
    assert len(bad_commands) == 3