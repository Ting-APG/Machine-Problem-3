import numpy as np

def modified_polyfit(inmat, deg):
    x = inmat[:,0];
    y = inmat[:,1];
    return np.polyfit(x,y,deg);
def modified_polyfitv2(inmat):
    x = inmat[:,0];
    y = inmat[:,1];
    retcoeff = np.polyfit(x,y,1);
    reterr = np.linalg.norm(y-np.polyval(retcoeff,x))
    for deg in range (2,10):
        curcoeff = np.polyfit(x,y,deg);
        curerr = np.linalg.norm(y - np.polyval(curcoeff,x) );
        if curerr < reterr:
            reterr = curerr;
            retcoeff = curcoeff;
            print(retcoeff)
    return retcoeff
    

matrix1 = np.array(np.mat('1 1; 2 2.0; 3 3; 4 4; 5 5; 6 6; 7 7; 8 8; 9 9; 10 10'));

output = modified_polyfitv2(matrix1);

