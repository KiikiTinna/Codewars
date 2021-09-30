#https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    for i in range(len(array)):
        elements=array[i]
        if elements == 0:
            array.remove(elements)
            array.append(elements)
    return array
