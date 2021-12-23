"""
This is test template explores the use of doctest
Test2
excecuting the test Python3 -m doctest -v 'Name of File'
"""

from doctest import testmod

def calc(a,b,c):
    
    """
    Takes the square and adds 3 numbers 
    >>> calc(3, 4, 5)
    50

    >>> calc(6, 2, 11)
    161

    """

    return a**2 + b**2 +c**2



# call the testmod function
if __name__ == '__main__':
    testmod(name ='calc', verbose = True)
