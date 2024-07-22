principal_amount = int(input('Enter the principle amount: '))
rate = int(input('Enter the annual interest rate: '))
durations = int(input('Enter the duration in years: '))

p = principal_amount
r = rate / 100 / 12
n = durations * 12

monthly_payment = p * (r* (1 + r)**n) / (((1 + r)**n)-1)
print ("monthly_amount" , monthly_payment)


