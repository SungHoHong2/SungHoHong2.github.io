from functools import reduce

def get_awesome_list(n, *args):
    result = []
    for i in range(n):
        element = ""
        for rule in args:
            div, text = rule
            element += text if (i+1)%div == 0 else ""
        result.append(element)

    return result

print(get_awesome_list(100, (3, "fast"), (5, "campus")))


def get_awesome_list(n, *args):
    return [ "".join([rule[1] if (i+1)%rule[0] == 0 else "" for rule in args ])
             for i in range(n)
           ]

print(get_awesome_list(100, (3, "fast"), (5, "campus")))