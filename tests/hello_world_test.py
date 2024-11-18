import os
import pytest
from problems import hello_world as hw


def test_hello_world(capsys):
     """
        unit test for hcker rank "if then else" probelm
        https://www.hackerrank.com/challenges/py-hello-world/problem?isFullScreen=true
     """
     #
     hw.hello_world()
     expected = 'Hello World!\n'
     captured = capsys.readouterr()
     assert captured.out == expected
     