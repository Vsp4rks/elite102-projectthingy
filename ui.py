import main
import tkinter as tk


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("600x400")
        self.resizable(False, False)
        self.title("Bank App")

        self.create_widgets()

    def create_widgets(self):
        label_title = tk.Label(self, text="V.C.S. Banking", font=("Helvetica", 20))
        label_title.pack(pady=20)

        label_username = tk.Label(self, text="Username:", font=("Helvetica", 12))
        label_username.pack()

        entry_username = tk.Entry(self, width=20)
        entry_username.pack()

        label_password = tk.Label(self, text="Password:", font=("Helvetica", 12))
        label_password.pack()

        entry_password = tk.Entry(self, width=20, show="*")
        entry_password.pack()

        button_login = tk.Button(self, text="Login", command=lambda: self.login(entry_username.get(), entry_password.get()))
        button_login.pack(pady=10)

    def login(self, username, password):
        print(f"Username: {username}, Password: {password}")


    # label_title = tk.Label(self, text="MAIN APP", font=("Helvetica", 20))
    # label_title.pack(pady=20)

    # label_balance = tk.Label(self, text="Your Balance:", font=("Helvetica", 16))
    # label_balance.pack()
    # balance_value = tk.Label(self, text="placeholder") 
    # balance_value.pack()

    # button_balancecheck = tk.Button(self, text="Check your balance", command=self.checkbalance)
    # button_balancecheck.pack(pady=5)
    # button_deposit = tk.Button(self, text="Make a Deposit", command=self.deposit)
    # button_deposit.pack(pady=5)
    # button_withdraw = tk.Button(self, text="Make a Withdrawal", command=self.withdrawal)
    # button_withdraw.pack(pady=5)
    # button_create = tk.Button(self, text="Create New Account", command=self.accountcreate)
    # button_create.pack(pady=5)
    # button_delete = tk.Button(self, text="Delete Account", command=self.accountdelete)
    # button_delete.pack(pady=5)

if __name__ == "__main__":
    app = Application()
    app.mainloop()