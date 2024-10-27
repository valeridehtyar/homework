calls = 0
def count_calls() :
    global calls
    calls += 1

def string_info(string) :
    count_calls()
    return (len(string),string.upper(), string.lower())

def is_contains(string, strings) :
    count_calls()
    return string.lower() in map(str.lower, strings)

print(string_info('Carybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban','BaNaN','urBAN']))# Urban ~ urBAN
print(is_contains('cycle',['recycling','cyclic']))# No matches
print(calls)
