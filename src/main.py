import tkinter as tk 
from tkinter import messagebox  
import ttkbootstrap as ttk  
import tkmacosx as tkm 
import sqlite3   
import bcrypt


class Users:
    def __init__(self):
        # Connects to an accounts database 
        self.connection = sqlite3.connect("temp_accounts.db") # Temporary database for testing  
        self.cursor = self.connection.cursor() 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(username PRIMARY KEY, password)")        

    def add_account(self, username, password):
        # Adds a new account to the database  
        try:
            self.cursor.execute("INSERT INTO users VALUES(?, ?)", (username, password)) 
            self.connection.commit()
        except:
            messagebox.showinfo(message = "Username already taken, choose another username")  

    def get_account(self, username, password):
        res = self.cursor.execute("SELECT password FROM users WHERE username = ?", (username))  
        try:
            hashed_password = res.fetchone()[0]
            if self.verify_password(password, hashed_password):
                print ("It matches!") 
            else:
                print("It does not match")
        except:
            print("Username does not exist") 
        

    def list_accounts(self):
        # Lists all accounts inside the database 
        res = self.cursor.execute("SELECT * FROM users")  
        print(res.fetchall())  
    
    def hash_password(self, password): 
        salt = bcrypt.gensalt() 
        hashed_password = bcrypt.hashpw(password.encode(), salt)  
        return hashed_password.decode() 
    
    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode()) 
    
     

class Account: 
    def __init__(self, username, password):
        self.username = username 
        self.password = password 

    # User account methods 
        # Add a login to the vault 
        # Remove a login from the vault 
        # get passwords of an account  

class Gui(tk.Toplevel):
    def __init__(self, parent): 
        super().__init__(parent) 
        self.parent = parent  
        self.parent.withdraw()
        self.title("Hello world")  
        self.geometry("500x500")    
        self.style = ttk.Style() 
        self.__create_sidebar()
        self.__create__widgets()  
        self.__events() 

    def on_enter(self, event): 
        print(self.focus_get())  
    
    def on_mousepress(self, event):
        pass
         
    def __events(self): 
        self.bind("<Return>", self.on_enter)  
        self.bind("<Button-1>", self.on_mousepress)       
    
    def __create_sidebar(self): 
        pass 
         
    def __create__widgets(self):  
        # Searchbar   
        self.searchbar = ttk.Entry(self)     
        self.searchbar.pack(side = 'top', padx = 5, pady = 5)   
        self.searchbar.bind("")
        # Sidebar 
        self.sidebar_frame = ttk.Frame(self)
        self.sidebar_frame.pack(side = 'left', expand = True, fill = 'both')  

        v = tk.StringVar(self.sidebar_frame, "allitems") 
        values = {
            "All items" : "allitems", 
            "Favourites" : "favourites", 
            "Bin" : "bin" 
        } 

        for (text, value) in values.items(): 
            self.style.configure("TRadiobutton", indicatoron = False) 
            ttk.Radiobutton(self.sidebar_frame, text = text, variable = v, value = value).pack(fill = 'x', ipady = 10, padx = 10)   
        # Main bar  
        self.vault_frame = tkm.SFrame(self) 
        self.vault_frame.pack(side = 'left', expand = True, fill = 'both')  
        ttk.Label(self.vault_frame, text = "this is the vault frame").pack() 

        # Config bar  
        self.config_frame = tkm.SFrame(self)
        self.config_frame.pack(side = 'left', expand = True, fill = 'both') 
        ttk.Label(self.config_frame, text = "this is the config frame").pack() 

    def logout(self): 
        self.destroy()
        self.parent.deiconify() 

class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.style = ttk.Style("darkly")
        self.title("Password Manager") 
        self.geometry("500x500")  
        self.username = tk.StringVar() 
        self.password = tk.StringVar()  
        self.users = Users() 
        self.__create_widgets()  
    
    
    def create_window(self):
        # Creates a window for the GUI
        # Refactor it into a class later  
        pass
                

    def sign_in(self): 
        username = self.username.get() 
        password = self.password.get()   
        account = Account(username, password) 
        res = self.users.get_account(username, password) 
        # self.create_window()  
        gui = Gui(self)  

    def create_account(self):
        username = self.username.get() 
        password = self.password.get()  
        hashed_password = self.users.hash_password(password) 
        new_account = Account(username, password)  
        self.users.add_account(username, hashed_password)  
        self.users.list_accounts() 

    def __create_widgets(self): 
        self.title_frame = ttk.Frame(self) 
        self.title_frame.pack(side = 'top', expand = True, fill = 'both')     

        self.app_title = ttk.Label(self.title_frame, text = "Bitwarden", font = "Calibri 32 bold" )  
        self.app_title.pack(side = 'top', expand = True, fill = 'y')    

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
    app.users.connection.close()  


