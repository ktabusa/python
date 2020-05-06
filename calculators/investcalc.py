import datetime
import math
import calendar

goal_subs = 100000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200

days_to_go = math.ceil(subs_to_go / avg_subs_day)
# take the ceiling of the value above, rounds up - 150.4 = 151

today = datetime.date.today()

print(today + datetime.timedelta(days=days_to_go))

print(' ')

print('Basic 2% a day Income from $1k to $100k\n')

start_date = datetime.date.today()
end_date = start_date


goal_account = 100000
current_account = 1000
income_left = goal_account - current_account
avg_income_day = 20
days_left = math.ceil(income_left / avg_income_day)

print(f'{days_left} Market Days to Goal')
print(today + datetime.timedelta(days=days_left))


print('2% Compounding Income from $1k to $100k')
print(' ')

income_to_date = 0
acct_balance = 1000
print(start_date, acct_balance)

while acct_balance < 100000:
    if end_date.weekday() < 5:
        percentage_income_day = .02
        acct_income = acct_balance * percentage_income_day
        acct_balance += acct_income
        acct_balance = round(acct_balance, 2)
        income_to_date = income_to_date + acct_income
        print(end_date, acct_balance, round(acct_income, 2))

    end_date = end_date + datetime.timedelta(days=1)
print(' ')
print(f'Reached $100,000 in {(end_date - start_date).days // 7} weeks.')
print(f'Took {(end_date - start_date).days} total days.')

weekends = (end_date - start_date).days
weekends = float(weekends)
weekends = float(weekends / 7)
weekends = math.floor(weekends) * 2 - 4
# -4 is to account for the start, end day, and the weekend days of the partial

print(f'Took {(end_date - start_date).days - weekends} days the stock market was open.')
