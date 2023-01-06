#Inputs taking time and hourly rate.
#Also factors in overtime at time-and-a-half.
#Created as a function,
#this code can also be run in compute_pay.py file

print('')
def computepay():
    print('Weekly Pay Calculator - Gross')
    try:
        h = input('Hours worked: ')
        r = input('Hourly rate: $')
        hours = float(h)
        rate = float(r)
        if hours > 40:
            pay = round(float(40 * rate),2)
            ot = ((hours - 40) * (rate * 1.5))
            total = round((pay + ot),2)
            print('Usual weekly pay: $',pay)
            print('Pay this week with overtime $',total)
        else:
            pay = round(float(hours * rate),2)
            print('Pay is $', pay)
    except:
        print('Sorry! This program only accepts numeric values.')





    
