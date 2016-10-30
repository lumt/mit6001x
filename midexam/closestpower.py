def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    if num < base:
    	return 0

    power = 2
    while base**power < num:
        power += 1
        
    if (num - base**(power-1)) <= (base**power - num):
        return power - 1
    else:
        return power