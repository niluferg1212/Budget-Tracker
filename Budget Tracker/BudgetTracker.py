import csv
import os
import matplotlib.pyplot as plt 
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog
 
user_file = "users.csv"
income_file = "income.csv"
expense_file = "expense.csv"
savings_file = "savings.csv"
 
files = [user_file, income_file, expense_file, savings_file]
for file in files:
    if not os.path.exists(file):
        with open(file, "w", newline='') as f:
            pass 

def user_login_check(userid, authKey):
    with open(user_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                stored_user = row[0].strip()
                stored_pass = row[1].strip()
                if stored_user == userid and stored_pass == authKey:
                    return True
    return False

def create_user_account(userid, authKey):
    with open(user_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([userid, authKey])

def record_user_income(userid, quantity, frequency):
    with open(income_file, 'a', newline='') as f:
        writer = csv.writer(f)
        current_time = datetime.now()
        writer.writerow([userid, quantity, frequency, current_time])

def record_user_expense(userid, category, quantity):
    with open(expense_file, 'a', newline='') as f:
        writer = csv.writer(f)
        current_time = datetime.now()
        writer.writerow([userid, category, quantity, current_time])

def define_savings_target(userid, aim, deadline):
    with open(savings_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([userid, aim, deadline])

def calculate_current_balance(userid):
    total_income = 0
    total_expenses = 0
    with open(income_file, newline='') as f:
        for row in csv.reader(f):
            if row and row[0] == userid:
                total_income += float(row[1])
    with open(expense_file, newline='') as f:
        for row in csv.reader(f):
            if row and row[0] == userid:
                total_expenses += float(row[2])
    return total_income - total_expenses

def generate_expense_summary(userid):
    summary = {}
    with open(expense_file, newline='') as f:
        for row in csv.reader(f):
            if row and row[0] == userid:
                category = row[1]
                quantity = float(row[2])
                summary[category] = summary.get(category, 0) + quantity
    return summary

def display_pie_chart(userid):
    data = generate_expense_summary(userid)
    if data:
        plt.figure(figsize=(6, 6))
        plt.pie(data.values(), labels=data.keys(), autopct='%1.2f%%')
        plt.title(f"{userid}'s Spending Report")
        plt.show()
    else:
        messagebox.showinfo("Info", "Nothing to display — you're either saving a lot or just getting started!")

class BudgetApp:
    def __init__(self, master):
        self.master = master
        master.title("Budget Tracker")
        self.userid = "" 
        self.display_login_interface() 

    def display_login_interface(self):
        self.clear()
        tk.Label(self.master, text="User ID").pack()
        self.userid_entry = tk.Entry(self.master)
        self.userid_entry.pack()

        tk.Label(self.master, text="Authentication Key:").pack()
        self.authKey_entry = tk.Entry(self.master, show="*")
        self.authKey_entry.pack()

        tk.Button(self.master, text="User Access", command=self.process_user_login).pack()
        tk.Button(self.master, text="Enroll", command=self.process_user_register).pack()

    def process_user_login(self):
        self.userid = self.userid_entry.get()
        authKey = self.authKey_entry.get()
        if user_login_check(self.userid, authKey):
            self.load_main_dashboard()
        else:
            messagebox.showerror("Error", "Try again with correct login info.")

    def process_user_register(self):
        userid = self.userid_entry.get()
        authKey = self.authKey_entry.get()
        if userid and authKey:
            create_user_account(userid, authKey)
            messagebox.showinfo("Done", "Account created")
        else:
            messagebox.showerror("Warning", "Fields cannot be blank.")

    def load_main_dashboard(self):
        self.clear()
        tk.Label(self.master, text=f"Hi {self.userid}, ready to manage your money?").pack()
        tk.Button(self.master, text="Add New Income", command=self.prompt_income_entry).pack()
        tk.Button(self.master, text="Record an Expense", command=self.prompt_expense_entry).pack()
        tk.Button(self.master, text="Check My Balance", command=self.display_balance).pack()
        tk.Button(self.master, text="Create a Savings Goal", command=self.prompt_savings_goal_entry).pack()
        tk.Button(self.master, text="See Spending Breakdown", command=self.show_chart).pack()
        tk.Button(self.master, text="Log Out", command=self.display_login_interface).pack()

    def prompt_income_entry(self):
        try:
            quantity = float(simpledialog.askstring("Income", "Enter income amount:"))
            frequency = simpledialog.askstring("Frequency", "Enter frequency (e.g. monthly):")
            if quantity < 0:
                raise ValueError
            record_user_income(self.userid, quantity, frequency)
            messagebox.showinfo("Saved", "Income added successfully")
        except:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def prompt_expense_entry(self):
        try:
            category = simpledialog.askstring("Category", "Classify this expense:")
            quantity = float(simpledialog.askstring("Amount", "Expense amount:"))
            if quantity < 0:
                raise ValueError("Invalid input: Amount cannot be less than zero.")
            record_user_expense(self.userid, category, quantity)
            messagebox.showinfo("Saved", "Expense has been successfully recorded.")
        except:
            messagebox.showerror("Error", "Entry failed due to invalid input values.")
    
    def prompt_savings_goal_entry(self):
        try:
            aim = float(simpledialog.askstring("Set Target", "Input the savings goal in numbers:"))
            deadline = simpledialog.askstring("Expected Date", "Provide the deadline in YYYY-MM-DD format.")
            define_savings_target(self.userid, aim, deadline)
            messagebox.showinfo("Completed", "Savings goal setup is complete")
        except:
            messagebox.showerror("Validation Failed", "Input format or value is incorrect.")

    def display_balance(self):
        balance = calculate_current_balance(self.userid)
        messagebox.showinfo("Status", f"Remaining balance: £ {balance:.2f}")

    def show_chart(self):
        display_pie_chart(self.userid)

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()
    
def main():
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()