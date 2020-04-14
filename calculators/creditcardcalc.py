# module started 4/12/20

import datetime
import calendar

# months to pay a cc off

balance = 5000
interest_rate = .21
# 21% annual interest rate
monthly_payment = 500

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
# this returns a day of the week that the first of the month falls on]
# and the number of days in the month
print(days_in_current_month)
# returned (2, 30) = wednesday, 30 days total in may
# adding the index at the end provides just 30, days in the month
days_till_end_month = days_in_current_month - today.day
print(days_till_end_month)

start_date = today + datetime.timedelta(days=days_till_end_month + 1)
print(start_date)
# this will return the first day of next month

end_date = start_date
interest_to_date = 0
# placeholder
# func time
# calc monthly interest charge, add it to balance, subtract payment
# round balance

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment
    balance = round(balance, 2)
    interest_charge = round(interest_charge, 2)
    interest_to_date = interest_to_date + interest_charge

    if balance < 0:
        balance = 0
    print(end_date, balance, round(interest_to_date, 2))

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_in_current_month)

# L34: this line is the same as balance + interest_charge
# L36: this rounds balance to two decimals
# this could also be combined as a single line turnary conditional
# this allows us to set a value based on a conditional on one line
# balance = 0 if balance is < 0 else round(balance, 2)
# the above is clearer, second is just less code

# L41:this calcs the days in the next month, then adds them to the current mo


# weekly progress to a goal


# daily progress to a goal
