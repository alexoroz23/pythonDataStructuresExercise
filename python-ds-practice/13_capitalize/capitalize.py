def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    if len(phrase) == 0:
        return phrase

    # Capitalize the first letter of the first word
    result = phrase[0].upper()

    # Capitalize the remaining letters
    for i in range(1, len(phrase)):
        if phrase[i-1] == ' ':
            result += phrase[i].upper()
        else:
            result += phrase[i]

    return result