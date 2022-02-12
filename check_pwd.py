def check_pwd(input):
    if 8 <= len(input) <= 20:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        include_lower = False
        digit = '1234567890'
        include_digit = False
        upper = lower.upper()
        include_upper = False
        sym = '~`!@#$%^&*()_+-='
        include_sym = False
        no_illgal = True
        for i in input:
            if i in lower:
                include_lower = True
            if i in digit:
                include_digit = True
            if i in upper:
                include_upper = True
            if i in sym:
                include_sym = True
            if i not in lower and i not in digit and i not in upper and i not in sym:
                no_illgal = False

        return (include_lower and include_digit and include_upper and include_sym and no_illgal)
    else:
        return False
