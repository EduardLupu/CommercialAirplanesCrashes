URL = 'https://en.wikipedia.org/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft'
SAVED_INFORMATION = 'D:\\Github\\CommercialAirplanesCrashes\\InformationScraped.xlsx'
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
dates = []
number_of_accidents = 0

# SEASONS
seasons_value = [0,      0,      0,      0]
#           Spring, Summer, Autumn, Winter
#                0       1       2       3

# DAYS OF THE WEEK
days_value = [0,    0,   0,   0,   0,   0,   0]
#            Sun, Mon, Tue, Wed, Thu, Fri, Sat
#             0     1    2    3    4    5    6
# MONTHS
months_value = [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]
#               -, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
#               0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12

# Array with leading number of days values
t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

