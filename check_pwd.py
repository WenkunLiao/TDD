def check_pwd(input):
    if 8 <= len(input) <= 20:
        lower = 'abcdefghijklmnopqrstuvwxyz'
        include_lower = False
        for i in input:
            if i in lower:
                include_lower = True
        return include_lower
    else:
        return False
