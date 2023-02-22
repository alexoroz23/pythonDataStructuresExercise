def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    stack = []
    for paren in parens:
        if paren == "(":
            stack.append(paren)
        elif paren == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0