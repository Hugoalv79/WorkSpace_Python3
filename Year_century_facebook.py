from math import ceil

def centuryFromYear(year):
    test = year/100
    test = ceil(test)
    return test
        


print(centuryFromYear(1905))