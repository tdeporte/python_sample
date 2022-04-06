#!/usr/bin/env python

"""Tests for `tom_project` package."""

import pytest
import functions as fun

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_add():
    if(fun.add(1,1) == 2):
        assert True
    else:
        assert False

def test_substract():
    if(fun.subtract(2,1) == 1):
        assert True
    else:
        assert False
        
def test_multiply():
    if(fun.multiply(2,2) == 4):
        assert True
    else:
        assert False
        
def test_divide():
    if(fun.divide(4,2) == 2):
        assert True
    else:
        assert False
