#  Exercise 2: Rewrite your pay program using try and except so that your
#  program handles non-numeric input gracefully by printing a message and
#  exiting the program.

hours = input('Please enter amount of hours: ')
try:
    float_hours = float(hours)
except:
    print('Error, please enter numeric input')
    exit()
rate = input('Please enter rate per hour: ')
try:
    float_rate = float(rate)
except:
    print('Error, please enter numeric input')
    exit()
if hours > str(40):
    grossPay = 1.5 * float_rate * float_hours
else:
    grossPay = float_hours * float_rate
# converting to string to concatenate $ sign.
# Adding round(answer, 2) to show 2 decimals.
print('The Gross Pay Amount is:', "$"+str(round(grossPay, 2)))