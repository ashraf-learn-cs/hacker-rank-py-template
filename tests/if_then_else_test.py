import os
import pytest
from problems import if_then_else 


@pytest.mark.parametrize("test_input,expected", 
                         [
                             (1, 'Weird\n') ,       #  If n is is odd, print Weird
                             (3, 'Weird\n'),
                             
                             (2, 'Not Weird\n'),    #  If n is even and in the inclusive range of 2 to 5, print Not Weird
                             (4, 'Not Weird\n'),
                             
                             (6, 'Weird\n'),        #  If n is even and in the inclusive range of 6 to 20, print Weird
                             (8, 'Weird\n'),  
                             
                             (24, 'Not Weird\n'),   #  If n is even and greater than 20, print Not Weird
                             (26, 'Not Weird\n')                         
                          ]
                        )
def test_if_then_else(capsys, test_input, expected):
    """
      parameterized unit testing for hcker rank "if then else" probelm
      https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
    """
    if_then_else.if_then_else(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected