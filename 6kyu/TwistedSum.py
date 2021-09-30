#https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f


def compute_sum(n):
    arr=list(range(1,n+1))
    suma=0
    for i in arr:
        if i<10:
            suma+=i
        else:
            i_str=str(i)
            sumnum=0
            for j in range(len(i_str)):
                sumnum+=int(i_str[j])
            suma+=sumnum
    return suma
