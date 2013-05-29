'''
The purpose of the program is to find intersection of two functions g1(x) and g2(x) by the means of the previously written newton.py.
Furthermore once task is solved, we need to provide some visulation.
'''

from newton import solve

def intersect(g1vals,g2vals,x0):
    '''
    given two functions and initial guess this function returns their intersections
    '''
      
    x, iterations = solve(  lambda x: ( g1vals(x)[0] - g2vals(x)[0], g1vals(x)[1] - g2vals(x)[1] ) , x0)
    
    return x


def function1(x):
    '''
    implementation of linear function and its derivative
    one of the function on which we would test our workhorse
    '''
    return 2*x,2

def function2(x):
    '''
    implementation of quadratic function and its derivative
    one of the function on which we would test our workhorse
    '''
    return x**2, 2*x    

def test_intersect1():
    actual = intersect(function1,function2,5.)
    expected = 2
    assert abs(actual - expected) < 1e-14

def test_intersect2():
    actual = intersect(function1,function2,-5.)
    expected = 0
    assert abs(actual - expected) < 1e-14


if __name__=='__main__':
    test_intersect1()
    test_intersect2()
    print("all test are passed")

