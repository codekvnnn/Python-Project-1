class BankAccount:
    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening  = date_of_opening 
        self.balance = balance
        self.customer_name = customer_name
        
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
            
    def check_balance(self):
        print(f"Current balance is ${self.balance}.")
        
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance: ${self.balance}\n")   

# Input customer details
ac_no_1 = BankAccount(2345, "02-07-2031", 1000, "Toninho Takeo")
ac_no_2 = BankAccount(1234, "12-06-2021", 2000, "Astrid Rugile")
ac_no_3 = BankAccount(2312, "11-02-2019", 3000, "Orli Kerenza")
ac_no_4 = BankAccount(1395, "02-05-2021", 3000, "Luciana Chika")
ac_no_5 = BankAccount(6345, "04-03-2022", 4000, "Toninho Takeo")

print("Customer Details:")
ac_no_1.print_customer_details()
ac_no_2.print_customer_details()
ac_no_3.print_customer_details()
ac_no_4.print_customer_details()
ac_no_5.print_customer_details()