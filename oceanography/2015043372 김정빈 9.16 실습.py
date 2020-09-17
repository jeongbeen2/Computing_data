nday_year = []
year = 1961
leap_year = year % 4 == 0
while year <= 2020:
    if leap_year:
        day = 366
    else:
        day = 365
    nday_year.append(day)
    year += 1
print(nday_year)