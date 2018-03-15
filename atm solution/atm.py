""" Function section"""
def withdraw(balance, amount):
    amount_discount = amount

    while amount_discount > 0:
        if amount_discount >= 100:
            print 'give 100'
            amount_discount = amount_discount - 100
        elif amount_discount >= 50:
            print 'give 50'
            amount_discount = amount_discount - 50

        elif amount >= 10:
            print 'give 10'
            amount_discount = amount_discount - 10

        elif amount_discount >= 5:
            print 'give 5'
            amount_discount = amount_discount - 5

        else:
            print 'give', amount_discount
            amount_discount = 0

    return balance - amount


"""App Section"""
user_balance = raw_input('Please enter Balance: ')
if len(user_balance) > 0 and user_balance.isdigit() is True and int(user_balance) > 0:
    balance = int(user_balance)
    while (True):
        user_amount = raw_input('Please enter Amount (q for quit): ')
        print 'Current', balance
        if user_amount != 'q':
            if len(user_amount) > 0 and user_amount.isdigit() is True and int(user_amount) > 0:
                amount = int(user_amount)

                if balance < amount:
                    print "Can't give you all this money !!"
                    break;
                else:
                    balance = withdraw(balance,amount)
            else:
                print 'Please check the Amount'
                break;
        else:
            print 'Thank you for use ATM'
            break;
else:
    print 'Please check the Balance'

