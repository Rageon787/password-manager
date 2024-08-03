import tkinter as tk 
# from tkinter import ttk 
import ttkbootstrap as ttk  
import sqlite3 
 
class Users:
    def __init__(self):
        # Connects to an accounts database 
        pass  
    
    def add_account(self,):
        # Adds a new account to the database 
        pass 
    def find_account():
        # Finds an existing account with specified username 
        pass 
     

class Account: 
    def __init__(self, username, password):
        self.username = username 
        self.password = password 

    # User account methods 
        # Add a login to the vault 
        # Remove a login from the vault 



    


class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.style = ttk.Style("darkly")
        self.title("Password Manager") 
        self.geometry("500x500")  
        self.username = tk.StringVar() 
        self.password = tk.StringVar() 
        self.__create_widgets() 

    def sign_in(self): 
        username = self.username 
        password = self.password
        account = Account(username, password)  


    def create_account(self):
        username = self.username.get() 
        password = self.password.get() 
        new_account = Account(username, password) 


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
        self.username_entry.bind("<KeyRelease>", self.enable_button) 

        # password entry
        self.password_frame = ttk.Frame(self.up_frame)
        self.password_frame.pack(side = 'top', fill = 'x') 

        self.password_label = ttk.Label(self.password_frame, text = "Master Password") 
        self.password_label.pack(side = 'top', fill = 'x') 

        self.password_entry = ttk.Entry(self.password_frame, font = "Calibri 24", textvariable = self.password, show = '*')
        self.password_entry.pack(side = 'top', fill = 'x')   
        self.password_entry.bind("<KeyRelease>", self.enable_button) 

        # Sign-in and create buttons 
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(side = 'top', fill = 'x')    

        # Sign-in button
        self.signIn_btn = ttk.Button(self.button_frame, text = "Sign In", state = tk.DISABLED, command = self.sign_in)
        self.signIn_btn.pack(side = 'top', fill = 'x') 
        
        
        # Create button
        self.create_btn = ttk.Button(self.button_frame, text = "Create a new account", state = tk.DISABLED, command = self.create_account)
        self.create_btn.pack(side = 'top', fill = 'x')    

    def enable_button(self, event):
        if self.username.get() and self.password.get():
            self.signIn_btn['state'] = tk.NORMAL 
            self.create_btn['state'] = tk.NORMAL 
        else:
            self.signIn_btn['state'] = tk.DISABLED
            self.create_btn['state'] = tk.DISABLED 

         
if __name__ == "__main__": 
    app = App() 
    app.mainloop()
    