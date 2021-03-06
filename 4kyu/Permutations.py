
#https://www.codewars.com/kata/5254ca2719453dcc0b00027d


def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])
    elif len(string) > 2:
        for i, j in enumerate(string):
            for k in permutations(string[:i] + string[i + 1:]):
                result.add(j + k)
    return list(result)
