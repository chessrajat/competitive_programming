
from datetime import date, timedelta

def dayOfProgrammer(year):
    non_leap = f"13.09.{year}"
    leap = f"12.09.{year}"
    trans = "26.09.1918"
    if year == 1918:
        return trans

    if year < 1918:
        if (year%4) == 0:
            return leap
        else:
            return non_leap
    else:
        if(year%400) == 0:
            return leap
        elif((year % 4) == 0 and (year%100) != 0):
            return leap
        else:
            return non_leap

      

if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)