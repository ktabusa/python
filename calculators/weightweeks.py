# 04/12/20 started part 2 of calculating days, weeks months module

import datetime

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
end_date = start_date

print(datetime.date.today())

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week


print('Ending Weight and Date')
print(end_date, current_weight)
print(' ')
print(f'Reached goal in {(end_date - start_date).days // 7} weeks')
