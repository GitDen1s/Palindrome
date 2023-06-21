def CheckPalindrome(user_input):
    chars = list(user_input)
    is_bool=False
    while len(chars) > 1:
        if chars.pop(0) != chars.pop():
            is_bool=False
        else:
            is_bool=True
    print(is_bool)

CheckPalindrome("лепсспел")