'''
The purpose of the program is to find intersection of two functions g1(x) and g2(x) by the means of the previously written newton.py.
Furthermore once task is solved, we need to provide some visulation.
'''

from newton import solve
import pylab as py
import numpy as np

def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def intersect(g1vals,g2vals,x0):
    '''
    given two functions and initial guess this function returns their intersections
    '''
      
    x, iterations = solve(  lambda x: ( g1vals(x)[0] - g2vals(x)[0], g1vals(x)[1] - g2vals(x)[1] ) , x0)
    
    return x

def find_intersections(g1vals,g2vals, lower_bound, upper_bound, number_of_guesses):
    '''
    given two functions, the range and the number of quessses to try, it returns all intersections found
    ''' 
    results = list()
    step = float( upper_bound - lower_bound) / float(number_of_guesses)
    for x0 in xfrange(lower_bound, upper_bound, step ):
         try:
            x = intersect(g1vals,g2vals,x0)
            results.append(x)
         except ZeroDivisionError:
             pass
    
    unique_results = np.unique(np.array(results).round(decimals=14)).tolist()
    
    return unique_results
    
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

def test_find_intersections1():
    actual = find_intersections(function1,function2, -5, 5, 20)
    expected = [0, 2]
    assert len(actual) == len(expected)
    assert sorted(actual) == sorted(expected)
    
if __name__=='__main__':
    print('let"s go')
    test_intersect1()
    test_intersect2()
    test_find_intersections1()
    print("all test are passed")
    
    X = np.linspace(-5, 5, 101, endpoint = True )
    Y1 = function1(X)[0]
    Y2 = function2(X)[0]
    
    py.plot(X, Y1, color='green')
    py.plot(X, Y2, color='blue')
    
    x = np.array( find_intersections(function1,function2, -5, 5, 10) )
    y = function1(x)[0]
    
    py.plot(x,y,'ko')
    
    py.xlim(  X.min() - 1, X.max() + 1)

    py.show()
    
    

