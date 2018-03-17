class ATM:

    def __init__(self):
        self.withdraw()


    def withdraw (self):
        user_balance = raw_input('Please enter Balance: ')
        user_bank_name = raw_input("Enter The bank name:")

        if self.v_input(user_balance, True) is True and self.v_input(user_bank_name, False) is True :
            self.balance = int(user_balance)
            bank_name = user_bank_name
        else:
            print 'Please check the Balance Or Bank Name'
            return

        while (True):
            user_amount = raw_input('Please enter Amount (q for quit): ')

            self.dash(30)
            self.dash(30)
            print 'Welcome to %s' %bank_name
            print 'Current Balance = %d' %self.balance
            self.dash(30)

            if user_amount != 'q':
                if self.v_input(user_amount, True) is True :
                    amount = int(user_amount)
                    if self.balance < amount:
                        print "Can't give you all this money !!"
                        break;
                    else:
                        self.balance = self.rebate_money(amount)
                else:
                    print 'Please check the Amount'
                    break;
            else:
                print 'Thank you for use ATM'
                break;
            self.dash(45)


    def v_input(self, item, type = True):
        if type is True:
            if len(item) > 0 and item.isdigit() is True and int(item) > 0:
                return True
        else:
            if len(item) > 0 and item.isdigit() is False:
                return True


    def dash (self, time = 40):
        print '-' * time


    def rebate_money(self, amount):
        rebate = amount
        while rebate > 0:
            for bnote in [100,50,10,5,1]:
                while rebate >= bnote:
                    if bnote >= 5:
                        print 'give %d' %bnote
                        rebate = rebate - bnote
                    else:
                        print 'give %d' %rebate
                        rebate = 0

        self.balance -= amount

        return self.balance