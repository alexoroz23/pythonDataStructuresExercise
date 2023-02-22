def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    # split the string into words
    words = phrase.split()

    # capitalize the first letter of each word
    title_words = [word.capitalize() for word in words]

    # join the words back into a string
    title_phrase = ' '.join(title_words)

    return title_phrase