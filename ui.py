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



    def withdraw(self):
        withdraw_window = tk.Toplevel(self)
        withdraw_window.title("Withdraw Money")

        label_amount = tk.Label(withdraw_window, text="Amount to Withdraw:", font=("Helvetica", 12))
        label_amount.grid(row=0, column=0, pady=10)

        entry_amount = tk.Entry(withdraw_window, width=20)
        entry_amount.grid(row=0, column=1, padx=10)

        button_withdraw = tk.Button(withdraw_window, text="Withdraw", command=lambda: self.confirm_withdraw(entry_amount.get()))
        button_withdraw.grid(row=1, column=0, columnspan=2, pady=10)

        def confirm_withdraw(self, amount):
            try:
                amount = float(amount)
                if amount <= 0:
                    tk.messagebox.showerror("Error", "Invalid withdrawal amount. Please enter a positive value.")
                    return
                if amount > main.checkbalance():
                    tk.messagebox.showerror("Error", "Insufficient funds. Please enter a valid amount.")
                    return
                main.withdraw(amount)
                tk.messagebox.showinfo("Success", f"Successfully withdrawn ${amount} from your account.")
                withdraw_window.destroy()
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid withdrawal amount. Please enter a valid number.")
        pass

    def deposit(self):
        deposit_window = tk.Toplevel(self)
        deposit_window.title("Deposit Money")

        label_amount = tk.Label(deposit_window, text="Amount to Deposit:", font=("Helvetica", 12))
        label_amount.grid(row=0, column=0, pady=10)

        entry_amount = tk.Entry(deposit_window, width=20)
        entry_amount.grid(row=0, column=1, padx=10)

        button_deposit = tk.Button(deposit_window, text="Deposit", command=lambda: self.confirm_deposit(entry_amount.get()))
        button_deposit.grid(row=1, column=0, columnspan=2, pady=10)

        def confirm_deposit(self, amount):
            try:
                amount = float(amount)
                if amount <= 0:
                    tk.messagebox.showerror("Error", "Invalid deposit amount. Please enter a positive value.")
                    return
                main.deposit(amount)
                tk.messagebox.showinfo("Success", f"Successfully deposited ${amount} into your account.")
                deposit_window.destroy()
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid deposit amount. Please enter a valid number.")
        pass

    def checkbalance(self):
        balance = main.checkbalance()
        tk.messagebox.showinfo("Balance", f"Your balance is: ${balance}")
        pass

    def createaccount(self):
        new_account_window = tk.Toplevel(self)
        new_account_window.title("Create New Account")

        label_username = tk.Label(new_account_window, text="Username:", font=("Helvetica", 12))
        label_username.grid(row=0, column=0, pady=10)

        entry_username = tk.Entry(new_account_window, width=20)
        entry_username.grid(row=0, column=1, padx=10)

        label_password = tk.Label(new_account_window, text="Password:", font=("Helvetica", 12))
        label_password.grid(row=1, column=0, pady=10)

        entry_password = tk.Entry(new_account_window, width=20, show="*")
        entry_password.grid(row=1, column=1, padx=10)

        label_balance = tk.Label(new_account_window, text="Initial Balance:", font=("Helvetica", 12))
        label_balance.grid(row=2, column=0, pady=10)

        entry_balance = tk.Entry(new_account_window, width=20)
        entry_balance.grid(row=2, column=1, padx=10)

        button_create_account = tk.Button(new_account_window, text="Create Account", command=lambda: self.create_account(entry_username.get(), entry_password.get(), entry_balance.get()))
        button_create_account.grid(row=3, column=0, columnspan=2, pady=10)
        pass

    def deleteaccount(self):
            confirm_dialog = tk.messagebox.askyesno(
                "Delete Account", "Are you sure you want to delete your account? This action cannot be undone.")

            if confirm_dialog:
                self.destroy()
                main.accountdelete()
                tk.messagebox.showinfo("Success", "Your account has been deleted successfully.")
    pass

    button_withdraw = tk.Button(self, text="Withdraw", command=lambda: self.withdraw())
    button_withdraw.pack(pady=10)

    button_deposit = tk.Button(self, text="Deposit", command=lambda: self.deposit())
    button_deposit.pack(pady=10)

    button_checkbalance = tk.Button(self, text="Check Balance", command=lambda: self.checkbalance())
    button_checkbalance.pack(pady=10)

    button_createaccount = tk.Button(self, text="New Account", command=lambda: self.newaccount())
    button_createaccount.pack(pady=10)

    button_deleteaccount = tk.Button(self, text="Delete Account", command=lambda: self.delaccount())
    button_deleteaccount.pack(pady=10)



if __name__ == "__main__":
    app = Application()
    app.mainloop()