import re
string1 = "what is your name"

def func(string1):
    return re.sub('[a,e,i,o,u]', '', string1)

print(func(string1))