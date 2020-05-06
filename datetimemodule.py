# Corey's Datetime Module started 04/10/20


import datetime
# dont name the file the same title as import / module bc call will be wrong
# AttributeError: partially initialized module 'datetime' has no attribute 'date' (most likely due to a circular import)

import pytz
# imported for alternative constructors/timezones below


d = datetime.date(2019, 7, 25)
# print(d)

tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.weekday())
# # Monday is 0, Sunday is 6
# print(tday.isoweekday())
# Monday is 1, Sunday is 7
print('Adding Dates')
tdelta = datetime.timedelta(days=7)
print(tday)
print(tday + tdelta)
# there is likely a dunder add __add__ in the datetime module
# same can be performed for subtraction of dates

# date2 = date1 + timedelta
# timedelta = date1 + date2

# use this to calc days to birthday
print(' ')

bday = datetime.date(2020, 10, 14)
till_bday = bday - tday

print('Days until my Birthday')
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

print(' ')
print('Bday Day of Week')
print(bday.isoweekday())
print('My bday is on a Wednesday')

print(' ')
print('TIME')

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2019, 7, 25, 9, 30, 45, 100000)
# print(dt)
# print(dt.year)
# print(dt.minute)

tdelta = datetime.timedelta(hours=7)
print(dt + tdelta)


# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
# these would all be the same if our comp was superfast

# .today - current local datetime with a timezone of none
# .now - provides an option to pass in a TZ, if none used, same as above
# .utcnow - though it has utc, we did not provide TZ info, so all dates naive

print('--alternative contstructors in datetime')
# 14:45 in the video
# pip install pytz was runp reviously, and is more useful than the basiclib
# this is recommended to help us offset times / timezones
# UTC is recommended for timezones in pytz.

print(' ')
# dt = datetime.datetime(2019, 7, 25, 9, 30, 45, tzinfo=pytz.UTC)
# this adds a timezone offset to the end, so the date becomes tz aware
# print(dt)
print('Current UTC Time')
UTC_now = datetime.datetime.now(tz=pytz.UTC)
print(UTC_now)

print('Current UTC Time - Long way')
long_UTC = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(long_UTC)


print('Current Local PST Time')
PST_now = datetime.datetime.now(pytz.timezone('US/Pacific'))
print(PST_now)

# print('Timezone List')
# if a timezone lookup is required run this for-loop
# for tz in pytz.all_timezones:
#     print(tz)

print(' ')
print('Taking a Naive DT and making it TZ aware')

dt_naive = datetime.datetime.now()
print(dt_naive)
print('')
pacific_tz = pytz.timezone('US/Pacific')
# this pulls the Pacific Timezone
dt_naive = pacific_tz.localize(dt_naive)
# .localize is a pytz specific method, and it applies the tz to the time

print(dt_naive)
# .astimezone is the longer way, need to lookup

print(' ')
print('Displaying Date Times')
print('Current PST')
PST_now = datetime.datetime.now(pytz.timezone('US/Pacific'))
print(PST_now)

print(PST_now.isoformat())

print(PST_now.strftime('%B %d, %Y'))
# format codes are in the datetime library
# strftime - is string format time
# strptime - is string parse time
# strftime - datetime to a String
# strptime - String to a datetime


# if you want to go the other way and convert a dt to perform operations
print(' ')
print('Converting October 14, 1986')
dt_str = 'October 14, 1986'

DT = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(DT)

# took 4x video duration
