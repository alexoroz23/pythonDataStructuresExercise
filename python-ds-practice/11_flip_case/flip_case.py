def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ''  # Create an empty string to hold the modified string
    for char in phrase:  # Loop through each character in the input string
        if char.lower() == to_swap.lower():  # Check if the character matches the character to be swapped (case-insensitive)
            if char.isupper():  # Check if the character is uppercase
                result += char.lower()  # If it is uppercase, add the lowercase version to the result string
            else:
                result += char.upper()  # If it is lowercase, add the uppercase version to the result string
        else:
            result += char  # If the character doesn't match the character to be swapped, add it to the result string as-is
    return result  # Return the modified string