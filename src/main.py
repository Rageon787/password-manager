import tkinter as tk 
# from tkinter import ttk 
import ttkbootstrap as ttk  
import sqlite3 

class App(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.title("Password Manager") 
        self.geometry("500x500")  
        self.username = tk.StringVar() 
        self.password = tk.StringVar() 
        self.__create_widgets() 

    def sign_in(self):
        pass 

    def create_account(self):
        pass

    def __create_widgets(self): 
        self.title_frame = ttk.Frame(self) 
        self.title_frame.pack(side = 'top', expand = True, fill = 'both')     

        self.title = ttk.Label(self.title_frame, text = "Bitwarden", font = "Calibri 32 bold" )  
        self.title.pack(side = 'top', expand = True, fill = 'y')    

        # Username and password entry frame
        self.up_frame =  ttk.Frame(self)
        self.up_frame.pack(side = 'top', fill = 'x', padx = 10, pady = 10)  

        # Username entry
        self.username_frame = ttk.Frame(self.up_frame)
        self.username_frame.pack(side = 'top', fill = 'x')

        self.username_label = ttk.Label(self.username_frame, text = "Username")
        self.username_label.pack(side = 'top', fill = 'x') 

        self.username_entry = ttk.Entry(self.username_frame, font = "Calibri 24", textvariable = self.username) 
        self.username_entry.pack(side = 'top', fill = 'x')  

        # password entry
        self.password_frame = ttk.Frame(self.up_frame)
        self.password_frame.pack(side = 'top', fill = 'x') 

        self.password_label = ttk.Label(self.password_frame, text = "Master Password") 
        self.password_label.pack(side = 'top', fill = 'x') 

        self.password_entry = ttk.Entry(self.password_frame, font = "Calibri 24", textvariable = self.password)
        self.password_entry.pack(side = 'top', fill = 'x')   


        # Sign-in and create buttons 
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(side = 'top', fill = 'x')    

        # Sign-in button
        self.signIn_btn = ttk.Button(self.button_frame, text = "Sign In", command = self.sign_in)
        self.signIn_btn.pack(side = 'top', fill = 'x') 
        
        
        # Create button
        self.create_btn = ttk.Button(self.button_frame, text = "Create a new account", command = self.create_account)
        self.create_btn.pack(side = 'top', fill = 'x')    

class User():
    pass

if __name__ == "__main__": 
    app = App() 
    app.mainloop()
    