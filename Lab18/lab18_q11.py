def isMagicDate(month, day, year):
    return month * day == year % 100

for year in range(1901, 2001):
    for month in range(1, 13):

        if month in (4, 6, 9, 11):
            last_day = 30
        elif month == 2:
            if year % 400 == 0 or (
                year % 4 == 0 and year % 100 != 0
            ):
                last_day = 29
            else:
                last_day = 28
        else:
            last_day = 31

        for day in range(1, last_day + 1):
            if isMagicDate(month, day, year):
                print(month, day, year)