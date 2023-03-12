import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ExoCalc")
        #self.iconbitmap("eggso.ico") 
        self.geometry("700x550")

        self.configure(bg="#333333")  # Set background colo.
        
        # Create entry widget to display calculations.
        self.entry = tk.Entry(self, width=30, font=("Helvetica", 16), bg="#222222", fg="#FFFFFF")
        self.entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
        
        # Create buttons for numbers and operators.
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)
        
        # Create button to clear entry widget.
        self.clear_button = tk.Button(self, text="C", width=8, height=2, font=("Helvetica", 16), bg="#008000", fg="#FFFFFF", command=self.clear)
        self.clear_button.grid(row=5, column=0, columnspan=2)
        
        # Create delete button to remove last character.
        self.delete_button = tk.Button(self, text="Del", width=8, height=2, font=("Helvetica", 16), bg="#FF0000", fg="#FFFFFF", command=self.delete_last)
        self.delete_button.grid(row=5, column=2, columnspan=2)
        
        # Create button to quit the application.
        self.quit_button = tk.Button(self, text="Quit", width=8, height=2, font=("Helvetica", 16), bg="#FFA500", fg="#FFFFFF", command=self.quit)
        self.quit_button.grid(row=6, column=0, columnspan=4, pady=10)
    
    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, width=8, height=3, font=("Helvetica", 16), bg="#000000", fg="#FFFFFF", command=lambda:self.click(text))
        button.grid(row=row, column=column)
    
    def click(self, text):
        if text == "=":
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif text == "Del":
            current_text = self.entry.get()
            self.entry.delete(len(current_text)-1, tk.END)
        else:
            self.entry.insert(tk.END, text)
    
    def clear(self):
        self.entry.delete(0, tk.END)
    
    def delete_last(self):
        current_text = self.entry.get()
        self.entry.delete(len(current_text)-1, tk.END)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
