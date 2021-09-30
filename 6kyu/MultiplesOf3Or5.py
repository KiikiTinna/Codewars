#https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    if number <= 0:
        return 0 
    suma=0
    arr= list(range(1, number))
    newarr=[]
    for i in arr:
      if i%3==0:
        suma+=i
        newarr.append(i)
      if i%5==0:
        if i not in newarr:
          suma+=i
          newarr.append(i)
    return suma  
