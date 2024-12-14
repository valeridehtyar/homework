


def get_multiplied_digits( number) :
    str_number = str(number).rstrip('0')
    if len(str_number) > 1 :
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)

result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)
print(result)
print(result2)