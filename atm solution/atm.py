user_amount = input('Please enter Amount: ')
user_balance = input('Please enter Balance: ')
amount = user_amount
if user_balance > user_amount and user_balance > 0 and user_amount > 0 :
    while amount > 0 :
        if amount >= 100:
            print 'give 100'
            amount = amount - 100
        elif amount >= 50:
            print 'give 50'
            amount = amount - 50

        elif amount >= 10:
            print 'give 10'
            amount = amount - 10

        elif amount >= 5:
            print 'give 5'
            amount = amount - 5

        elif amount >= 2:
            print 'give 2'
            amount = amount - 2
        elif amount == 1:
            print 'This is the remaining:', amount
            total = user_balance - user_amount + amount
            print 'Balance remaining', total
            amount = amount - 1
        else:
            print 'The full amount has been withdraw'
            total = user_balance - user_amount
            print 'Balance remaining', total

else:
    if user_balance > 0 or user_amount > 0 :
        print "please check th input"
    else:
        print "The existing balance is insufficient"
