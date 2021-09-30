#https://www.codewars.com/kata/5e2596a9ad937f002e510435

def infected(s):
    countX=s.count("X")
    if countX ==len(s):
        return 0
    islands=s.split("X")
    infected = 0
    uninfected = 0
    for i in islands:
        if "1" in i:
            infected+=len(i)
        else:
            uninfected+=len(i)
    total=(infected+uninfected)
    return infected/total*100
