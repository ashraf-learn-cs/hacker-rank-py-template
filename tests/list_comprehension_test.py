import os
import pytest

from problems import List_comprehensions as lc



@pytest.mark.parametrize("x,y,z,n,expected", 
                         [
                            (1,1,1,2,
                              [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
                            ), 
                            (2,2,2,2,
                              [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]  
                            )
                            
                          ]
                        )
def test_list_comprehension_1(x,y,z,n, expected):
    #x = 1 
    #y = 1
    #z = 1
    #n = 2
    #expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    
    result = lc.list_comp(x,y,z,n)
    
    assert result == expected


#def test_list_comprehension_2():
#    x = 2 
#    y = 2
#    z = 2
#    n = 2
#    expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
#
#    
#    result = lc.list_comp(x,y,z,n)
#    
#    assert result == expected