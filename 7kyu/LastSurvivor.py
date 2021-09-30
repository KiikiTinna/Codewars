#https://www.codewars.com/kata/609eee71109f860006c377d1


def last_survivor(letters, coords):
    old_string = letters
    for i in range(len(coords)):
        string_list = list(old_string)
        index=coords[i]
        string_list[index] = ""
        old_string = "".join(string_list)
    return old_string
