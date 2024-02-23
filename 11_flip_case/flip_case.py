def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new_string = ''

    for let in phrase:
        if let.lower() == to_swap.lower():
            new_string += let.swapcase()
        else:
            new_string += let

    return new_string
