def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

 # Return a new list with only elements that are considered True in a boolean context
    return [elem for elem in lst if elem]

    # elem is a variable used in the list comprehension to represent each element of the input list lst. In other words, it is a placeholder variable used to iterate over the elements of the list.