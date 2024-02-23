def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels_dict = {}

    for let in phrase:
        if let.lower() in 'aeiou':
            if let.lower() in vowels_dict:
                vowels_dict[let.lower()] += 1
            else:
                vowels_dict[let.lower()] = 1
    return vowels_dict
