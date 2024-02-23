def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    left = 0
    right = len(phrase) - 1

    def move_past_space(left, right):
        while phrase[left] == ' ':
            left += 1

        while phrase[right] == ' ':
            right -= 1

        return left, right
        

    while left < right:
        left, right = move_past_space(left, right)
        if phrase[left].lower() == phrase[right].lower():
            left += 1
            right -= 1
        else:
            return False
    
    return True