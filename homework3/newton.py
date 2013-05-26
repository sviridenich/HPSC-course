# -*- coding: utf-8 -*-
'''
Python module newton.py that contains a function solve that takes the following inputs:
fvals, a function that returns the values of f(x) and f′(x) for any input x (see the example below),
x0, the initial guess,
debug, an optional argument with default False.
The function should return a tuple consisting of the final iterate (the approximation to the root determined) and the number of iterations taken.
'''

def solve(fvals,x0, debug = False):
    maxiter = 20
    tol = 1e-14
    
    if (debug):
        print "Initial guess is %22.15e" % x0
        
    x = x0
    for i in range(maxiter):
        
        if ((debug) & (i > 0 )):
            print "after %i iterations, x = %22.15e" %(i, x)
            
        fx,fxprime = fvals(x)
        if abs(fx) < tol :
            break
        x = x - fx/fxprime
        
    return (x, i)

def fvals_sqrt(x):
    """
    Return f(x) and f(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=True):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x

if __name__=="__main__":
    test1()