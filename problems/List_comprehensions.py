#------------------------------------------------------------------------------------------------
# URL........: https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
#
# Description:
#
#-------------------------------------------------------------------------------------------------

    # x = 1 
    # y = 1
    # z = 1
    # n = 2
    # expected = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    
    
def list_comp(x:int, y:int, z:int, n:int):
    final_list = []
    #x_list = [i for i in range(0,x+1)]
    #y_list = [i for i in range(0,y+1)]
    #z_list = [i for i in range(0,z+1)]
    #
    #print ('x_list' ,  x_list)
    #print ('y_list' ,  y_list)
    #print ('z_list' ,  z_list)
    #
    #working_list = [ [x, y,z ] for x in x_list for y in y_list for z in z_list]
    #
    #print(working_list)
    ## remove inner list with sum = 2
    #final_list = [ x for x in working_list if sum(x) != 2]
    
    return final_list



if __name__ == '__main__':
#    print(list_comp(1,1,1,2))
#    
    print(list_comp(2,2,2,2))
    
    print("ok")
    
    
    