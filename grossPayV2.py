#  Exercise 1
#  Rewrite your pay computation to give the employee 1.5 times
#  the hourly rate for hours worked above 40 hours.
hours = float(input('Please enter amount of hours: '))
rate = float(input('Please enter rate per hour: '))
if hours > 40:
    extraTime = hours - 40.0
    extraTimeRate = extraTime * 1.5 * rate
    grossPay = 40.0 * rate + extraTimeRate
else:
    grossPay = hours * rate
#  converting to string to concatenate $ sign.
#  Adding round(answer, 2) to show 2 decimals
print('The Gross Pay Amount is:', "$"+str(round(grossPay, 2)))