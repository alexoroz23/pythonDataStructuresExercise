def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # Convert numbers to strings
    str1 = str(num1)
    str2 = str(num2)

    # Count frequency of each digit in each string
    freq1 = {digit: str1.count(digit) for digit in str1}
    freq2 = {digit: str2.count(digit) for digit in str2}

    # Compare dictionaries
    return freq1 == freq2