from variables import *


def check_month(text):
    for month in months:
        if month in text:
            return True
    return False


def seasons():
    seasons_value[0] = months_value[3] + months_value[4] + months_value[5]  # Spring
    seasons_value[1] = months_value[6] + months_value[7] + months_value[8]  # Summer
    seasons_value[2] = months_value[9] + months_value[10] + months_value[11]  # Autumn
    seasons_value[3] = months_value[12] + months_value[1] + months_value[2]  # Winter


def percentage(x, y):
    return format(x * 100 / y, ".3f")


def days_of_the_week():
    for date in dates:
        date_split = date.split()  # e.g. February 6 2002

        if "January" in date_split:
            date_split[0] = 1
        if "February" in date_split:
            date_split[0] = 2
        if "March" in date_split:
            date_split[0] = 3
        if "April" in date_split:
            date_split[0] = 4
        if "May" in date_split:
            date_split[0] = 5
        if "June" in date_split:
            date_split[0] = 6
        if "July" in date_split:
            date_split[0] = 7
        if "August" in date_split:
            date_split[0] = 8
        if "September" in date_split:
            date_split[0] = 9
        if "October" in date_split:
            date_split[0] = 10
        if "November" in date_split:
            date_split[0] = 11
        if "December" in date_split:
            date_split[0] = 12

        y = int(date_split[2])
        m = int(date_split[0])
        d = int(date_split[1])

        # if month is less than 3 reduce year by 1
        if m < 3:
            y = y - 1

        result = (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7
        days_value[result] += 1


def add_months():
    for date in dates:
        if "January" in date:
            months_value[1] += 1
        if "February" in date:
            months_value[2] += 1
        if "March" in date:
            months_value[3] += 1
        if "April" in date:
            months_value[4] += 1
        if "May" in date:
            months_value[5] += 1
        if "June" in date:
            months_value[6] += 1
        if "July" in date:
            months_value[7] += 1
        if "August" in date:
            months_value[8] += 1
        if "September" in date:
            months_value[9] += 1
        if "October" in date:
            months_value[10] += 1
        if "November" in date:
            months_value[11] += 1
        if "December" in date:
            months_value[12] += 1

