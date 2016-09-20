


"""
def get_awesome_list(n, rule1, rule2):

    paramList = []
    paramList.append(rule1)
    paramList.append(rule2)

    for param in paramList:
        num, name = param

        for i in range(n):
            returnList.append(name) if (i+1)%num else ""

"""


def get_awesome_list(n, rule1, rule2):
        result =  []
        for i in range(n):
            element = ""
            for rule in [rule1, rule2]:
                div, text = rule
                element += text if (i+1)%div == 0 else ""
            result.append(element)
        return result



print(get_awesome_list(100, (3, "fast"), (5, "campus")))





