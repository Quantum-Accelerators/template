import numpy as np

def add(a: int, b: int) -> int:
    """
    A function that adds two numbers.

    Parameters
    ----------
    a
        First number to add.
    b
        Second number to add.
    
    Returns
    -------
    int
        The sum of a and b.
    
    """
    return a + b

def make_array(val: int, length: int = 3) -> np.ndarray:
    """
    A function to transform a number into a numpy array.

    Parameters
    ----------
    val
        Number to turn into an array.
    length
        The length of the array.
    
    Returns
    -------
    np.ndarray
        An array composed of `val`.
    """
    return np.array([val]*length)
