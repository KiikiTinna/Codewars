#https://www.codewars.com/kata/59377c53e66267c8f6000027

def alphabet_war(fight):
    leftside=0
    rightside=0
    for i in fight:
        if i == "w":
            leftside+=4
        elif i=="p":
            leftside+=3
        elif i=="b":
            leftside+=2
        elif i=="s":
            leftside+=1
        elif i=="m":
            rightside+=4
        elif i=="q":
            rightside+=3
        elif i=="d":
            rightside+=2
        elif i=="z":
            rightside+=1  
    if rightside>leftside:
        return "Right side wins!"
    elif rightside<leftside:
        return "Left side wins!"
    elif rightside==leftside:
        return "Let's fight again!"
