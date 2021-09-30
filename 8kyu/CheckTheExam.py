#https://www.codewars.com/kata/5a3dd29055519e23ec000074

def check_exam(arr1,arr2):
    skupaj=0
    for i in range(len(arr1)):
        if arr1[i]==arr2[i]:
            skupaj+=4
        if arr1[i]!=arr2[i] and arr2[i]!="":
            skupaj-=1
    if skupaj<=0:
        return 0
    else:
        return skupaj

