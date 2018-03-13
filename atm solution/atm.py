""" withdraw Function """
def withdraw(balance, amount):
    amount_discount = amount
    while amount > 0:
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

        else:
            print 'give', amount
            amount = 0

    return balance - amount_discount


user_balance = input('Please enter Balance: ')
balance = user_balance
if balance > 0:
    while(True):
        user_amount = raw_input('Please enter Amount (q for quit): ')
        amount = user_amount
        print 'Current', balance
        if amount > 0:
            if user_amount != 'q':
                if balance < int(amount) :
                    print "Can't give you all this money !!"
                    break;
                else:
                    balance = withdraw(balance, int(amount))
            else:
                print 'Thank you for use ATM'
                break;
        else:
            print 'Please check the Amount'
else:
    print 'Please check the Balance'



