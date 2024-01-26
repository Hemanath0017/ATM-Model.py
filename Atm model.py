#ATM simulator:
#crate a program that simulates the all atm functionlities and operation.(check balance,Deposit,withdraw)
class ATM:
    def withdraw(self, pin):
        bal = 10000
        if pin == 123:
            query = int(input("1. Check balance\n2. Withdraw\n3. Deposit\n4.Exit\nEnter your choice: "))
            if query == 1:
                print("Your balance is:", bal)
            elif query == 2:
                m_req = int(input("Enter the amount: "))
                if m_req > bal:
                    print("Insufficient balance")
                else:
                    bal -= m_req
                    print("Withdrawal successful. Your current balance is:", bal)
            elif query == 3:
                Deposit = int(input("How much you want to add:"))
                if Deposit > 0:
                    bal += Deposit
                    print("Amount Credited Successfully.Your current balance is:", bal)
                else:
                    print("Please check your amount")
            elif query == 4:
                print("Thank you for using ATM,Goodbye..")
            else:
                print("Invalid choice,Select your option 1,2,3,4 or 5")
        else:
            print("Invalid pin")

kvb = ATM()
pin = int(input("Enter your PIN: "))
kvb.withdraw(pin)


