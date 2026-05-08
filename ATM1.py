
#abstraction , encupsulation , inheritnce , Overriding , Polymorphism , Overloading , coperhention , tkiner

from abc import ABC , abstractclassmethod
import tkinter as tk
from tkinter import messagebox

class Account(ABC):
    def __init__(self , name , balance , pin):
        self._name = name
        self.__balance = balance
        self.__pin = pin
    
    @abstractclassmethod
    def withdraw(self,amount):
        pass

    def deposit(self , amount):
        self.__balance += amount


    def get_balance(self):
        return self.__balance 
    
    def check_pin(self , pin):
        return str(self.__pin) == str(pin).strip()
    
    def _modify_balance(self, amount):
        self.__balance += amount

class SavingAccount(Account):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._modify_balance(-amount)
        else:
            raise ValueError("Insufficient balance")

class CurrentAccount(Account):
    def withdraw(self, amount):
        self._modify_balance(-amount)

def perform_withdraw(account,amount):
    account.withdraw(amount)

class Transaction:

    def process(self,account,amount , typ1="deposit"):
        if typ1 == "deposit":
            account.deposit(amount)
        elif typ1 == "withdraw":
             account.withdraw(amount)

class ATM:
    def __init__(self , accounts):
        self.accounts = accounts
        self.current_account = None

    def login(self , name , pin):
        search_name = name.strip().lower()

        for acc in self.accounts:

            if acc._name.lower() == search_name and acc.check_pin(pin):
                self.current_account = acc
                return True
        
        return False
            
    def deposit(self , amount):
        self.current_account.deposit(amount)

    def withdraw(self , amount):
        perform_withdraw(self.current_account , amount)

    def get_balance(self):
        return self.current_account.get_balance()
    
accounts = [SavingAccount("Ali" , 20000 , "1322") , CurrentAccount("Sara" , 40000 , "3199")]
names = [acc._name for acc in accounts]
atm =ATM(accounts)

#tkiner:

root = tk.Tk()
root.title("ATM System")
root.geometry("300x300")

login_frame = tk.Frame(root)
login_frame.pack()


tk.Label(login_frame , text="Name").pack()
name_entry = tk.Entry(login_frame)
name_entry.pack()

tk.Label(login_frame, text="PIN").pack()
pin_entry = tk.Entry(login_frame, show="*")
pin_entry.pack()


def login():
    name = name_entry.get().strip().lower()
    pin = pin_entry.get().strip()

    if atm.login(name , pin):
        messagebox.showinfo("Success","Login Successful")
        login_frame.pack_forget()
        main_frame.pack()

    else:
        messagebox.showerror("Error" ,"Invalid Credentials")
    
tk.Button(login_frame , text="Login" , command=login).pack()

#Main_Frame:
main_frame = tk.Frame(root)

balance_lable = tk.Label(main_frame , text="Balance: ")
balance_lable.pack()

def show_balance():
    balance_lable.config(text=f"Balance: {atm.get_balance()}")

tk.Button(main_frame , text="Check Balance",command=show_balance).pack()

amount_entry = tk.Entry(main_frame)
amount_entry.pack()

def deposit():
    try:
        amount = float(amount_entry.get())
        atm.deposit(amount)
        messagebox.showinfo("Success" , "Deposit")
    except:
        messagebox.showerror("Error","Invalid Amount")

tk.Button(main_frame,text="Deposit",command=deposit).pack()

def withdraw():
    try:
        amount = float(amount_entry.get())
        atm.withdraw(amount)
        messagebox.showinfo("Success","Withdraw")
    except Exception as er:
        messagebox.showerror("Error",str(er))

tk.Button(main_frame,text="Withdraw",command=withdraw).pack()
root.mainloop()










    
        
        

        
        





    



        
