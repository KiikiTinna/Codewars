#https://www.codewars.com/kata/5865cff66b5699883f0001aa

def to_time(seconds):
    h=(seconds//3600)
    m = (seconds-h*60*60)//60
    return str(h)+" hour(s)"+" and " + str(m)+" minute(s)"
