def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_to_frequency1 = {}
    num_to_frequency2 = {}

    for num in str(num1):
        if num in num_to_frequency1:
            num_to_frequency1[num] += 1
        else:
            num_to_frequency1[num] = 1

    for num in str(num2):
        if num in num_to_frequency2:
            num_to_frequency2[num] += 1
        else:
            num_to_frequency2[num] = 1

    for num in num_to_frequency1:
        if num_to_frequency2[num]:
            if num_to_frequency1[num] == num_to_frequency2[num]:
                pass
            else:
                return False
        else:
            return False
        
    return True

    