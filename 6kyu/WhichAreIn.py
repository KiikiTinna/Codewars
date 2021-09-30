#https://www.codewars.com/kata/550554fd08b86f84fe000a58



def in_array(array1, array2):
    resoult = []
    for i in array1:
        for j in array2:
            if i in j and i not in resoult:
                resoult.append(i)
                break
    resoult.sort()
    return r
