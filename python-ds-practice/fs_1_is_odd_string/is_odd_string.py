def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # Define a function that computes the character position of a letter
    def char_position(char):
        return ord(char.lower()) - 96

    # Compute the sum of character positions for each letter in the word
    char_positions_sum = sum(char_position(char) for char in word)

    # Return True if the sum is odd, and False otherwise
    if char_positions_sum % 2 != 0:
        return True
    else:
        return False