def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    # loop an empty dictionary to store the results
    result = {}

    # loop through each letter in the phrase
    for letter in phrase:

        # if the letter is already in the dictionary, increment its count
        if letter in result:
            result[letter] += 1
        # otherwise, add the letter to the dictionary with a count of 1    
        else:
            result[letter] = 1
    # return the final result dictionary
    return result