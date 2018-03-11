user_amount = input('Please enter Amount: ')
user_balance = input('Please enter Balance: ')
amount = user_amount
if user_balance > user_amount :
    while amount >= 100:
        print 'give 100'
        amount = amount - 100
    while amount >= 50:
        print 'give 50'
        amount = amount - 50

    while amount >= 10:
        print 'give 10'
        amount = amount - 10

    while amount >= 5:
        print 'give 5'
        amount = amount - 5

    while amount >= 2:
        print 'give 2'
        amount = amount - 2

    if amount == 1:
        print 'This is the remaining:', amount
        total = user_balance - user_amount + amount
        print 'Balance remaining', total

    else:
        print 'The full amount has been withdraw'
        total = user_balance - user_amount
        print 'Balance remaining', total
else:
    print "The existing balance is insufficient"
