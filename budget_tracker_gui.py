import tkinter as tk
from tkinter import messagebox

class BudgetTrackerGui():
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")

root = tk.Tk()
app = BudgetTrackerGui(root)
root.mainloop()