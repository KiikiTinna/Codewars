#https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]
