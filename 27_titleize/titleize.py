def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    capitalized_phrase = ''

    for word in phrase.split(' '):
        capitalized_phrase += f'{word.capitalize()} '

    return capitalized_phrase.strip()