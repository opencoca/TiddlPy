import os
import pytest
import requests
from hypothesis import given, example
import hypothesis.strategies as st

from TiddlPy import loadtiddlers, searchtiddlers, findtiddlers, wikiedit

@pytest.fixture(scope='session')
def tiddlywikidotcom():
    filename = 'tempfile.html'
    r = requests.get('https://tiddlywiki.com')
    file = open(filename, 'wb')
    file.write(r.content)
    yield(filename)

def test_reading1(tiddlywikidotcom):
    t=loadtiddlers(tiddlywikidotcom, ['HelloThere'])
    print(t[0]['title'])
    assert t[0]['title'] == 'HelloThere'
    pass


    