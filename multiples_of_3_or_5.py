def solution(number):
    mult = 0
    i = 0
    while i < number:
        if (i%3 == 0) or (i%5 == 0):
            mult += i
        i += 1
    return mult
