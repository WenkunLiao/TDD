def check_pwd(input):
    if 8 <= len(input) <= 20:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        include_lower = False
        digit = '1234567890'
        include_digit = False
        upper = lower.upper()
        include_upper = False
        for i in input:
            if i in lower:
                include_lower = True
            if i in digit:
                include_digit = True
            if i in upper:
                include_upper = True
        return (include_lower and include_digit and include_upper)
    else:
        return False
