import tkinter as tk 
from tkinter import messagebox  
import ttkbootstrap as ttk  
import tkmacosx as tkm 
import sqlite3   
import bcrypt
import random  


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
    
     
class Config:
    def __init__(self, parent): 
        self.parent = parent 
        self.config_frame = tkm.SFrame(self.parent)
        self.config_frame.pack(side = 'left', expand = True, fill = 'both') 
        ttk.Label(self.config_frame, text = "hello world").pack() 

    def _empty_configFrame(self): 
        # Destroys all current widgets in the config frame 
        for child in self.config_frame.winfo_children():
            child.destroy()

    def _create_infoPane(self): 

        # Triggered when a user selects another login from the treeview 

        self._empty_configFrame()
        ttk.Label(self.config_frame, text = "ITEM INFORMATION").pack()  

        nameEntry_label = ttk.Label(self.config_frame, text = "Name") 
        nameEntry_label.pack()

        name_var = tk.StringVar()
        name_entry = ttk.Entry(self.config_frame, textvariable = name_var) 
        name_entry.pack()  

        usernameEntry_label = ttk.Label(self.config_frame, text = "Username")  
        usernameEntry_label.pack() 

        username_var = tk.StringVar()
        username_entry = ttk.Entry(self.config_frame, textvariable = username_var) 
        username_entry.pack()
        
        passwordEntry_label = ttk.Label(self.config_frame, text = "Password")  
        passwordEntry_label.pack()  

        password_var = tk.StringVar()
        password_entry = ttk.Entry(self.config_frame, textvariable = password_var) 
        password_entry.pack() 



    def _create_editPane(self): 

        # Triggers when a user wants to edit an item 

        self._empty_configFrame() 
        ttk.Label(self.config_frame, text = "EDIT ITEM").pack() 

        nameEntry_label = ttk.Label(self.config_frame, text = "Name") 
        nameEntry_label.pack()

        name_var = tk.StringVar()
        name_entry = ttk.Entry(self.config_frame, textvariable = name_var) 
        name_entry.pack()  

        usernameEntry_label = ttk.Label(self.config_frame, text = "Username")  
        usernameEntry_label.pack() 

        username_var = tk.StringVar()
        username_entry = ttk.Entry(self.config_frame, textvariable = username_var) 
        username_entry.pack()
        
        passwordEntry_label = ttk.Label(self.config_frame, text = "Password")  
        passwordEntry_label.pack()  

        password_var = tk.StringVar()
        password_entry = ttk.Entry(self.config_frame, textvariable = password_var) 
        password_entry.pack() 


    def _create_newLoginPane(self): 
        
        # Triggered when a user selects the "add a login" button 

        self._empty_configFrame()  

        operation_label = ttk.Label(self.config_frame, text = "ADD ITEM") 
        operation_label.pack()  

        nameEntry_label = ttk.Label(self.config_frame, text = "Name") 
        nameEntry_label.pack()

        name_var = tk.StringVar()
        name_entry = ttk.Entry(self.config_frame, textvariable = name_var) 
        name_entry.pack()  

        usernameEntry_label = ttk.Label(self.config_frame, text = "Username")  
        usernameEntry_label.pack() 

        username_var = tk.StringVar()
        username_entry = ttk.Entry(self.config_frame, textvariable = username_var) 
        username_entry.pack()
        
        passwordEntry_label = ttk.Label(self.config_frame, text = "Password")  
        passwordEntry_label.pack()  

        password_var = tk.StringVar()
        password_entry = ttk.Entry(self.config_frame, textvariable = password_var) 
        password_entry.pack() 

class Account: 
    def __init__(self, username, password):
        self.username = username 
        self.password = password 
        self.connection = sqlite3.connect(f"{self.username}.db")  
        self.cursor = self.connection.cursor() 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS vault(application TEXT, username TEXT, password TEXT)") 
        
    
    def get_logins(self):
        # returns a list of all logins from the vault    
        res = self.cursor.execute("SELECT * FROM vault")  
        return res.fetchall()   
 
    def add_login(self, application, username, password): 
        self.cursor.execute("INSERT INTO vault(application, username, password) VALUES(?, ?, ?)", (application, username, password))  
        self.connection.commit() 
        self.get_logins() 

class Gui(tk.Toplevel):
    def __init__(self, parent, account): 
        super().__init__(parent) 
        self.parent = parent   
        self.account = account
        self.parent.withdraw()
        self.title("Password manager")  
        self.geometry("1200x900")    
        self.style = ttk.Style()  
        self.__create__widgets()  
        self.__events()  
        self.config = Config(self) 

    def on_enter(self, event): 
        print(self.focus_get())  
    
    def on_mousepress(self, event):
        pass
         
    def __events(self): 
        self.bind("<Return>", self.on_enter)  
        self.bind("<Button-1>", self.on_mousepress)       
    
    def add_login(self):  
        self.config._create_newLoginPane()
        # letters = ("abcdefghijklmnopqrstuvwxyx") 
        # application = "".join(random.choice(letters) for i in range(5))
        # username = "".join(random.choice(letters) for i in range(8)) 
        # password = "".join(random.choice(letters) for i in range(10))    
        # self.vault_tree.insert("", tk.END, values = (application, username, password))
        # self.account.add_login(application, username, password) 
        

    def __create_vault_frame(self):
        # Main bar  
        self.vault_frame = tkm.SFrame(self) 
        self.vault_frame.pack(side = 'left', expand = True, fill = 'both')  
        
        columns = ("application", "username", "password") 

        self.vault_tree = ttk.Treeview(self.vault_frame, columns = columns, show = 'headings') 
       
        self.vault_tree.heading("application", text = "Application") 
        self.vault_tree.heading("username", text = "Username")  
        self.vault_tree.heading("password", text = "Password")  

        logins = self.account.get_logins() 

        self.vault_tree.pack(expand = True, fill = 'x') 
        
        for login in logins:
            self.vault_tree.insert('', tk.END, values=login) 

            
    def __create_add_button(self):
        self.vaultAdd_btn = ttk.Button(self.vault_frame, text = "Add a login", command = self.add_login)  
        self.vaultAdd_btn.pack(expand = True, fill = 'x') 
        
    def __create_searchbar(self):
        self.searchbar = ttk.Entry(self)     
        self.searchbar.pack(side = 'top', padx = 5, pady = 5)   
        self.searchbar.bind("")

    def __create__widgets(self): 
        self.__create_searchbar()
        self.__create_vault_frame()
        self.__create_add_button() 

    def logout(self): 
        self.destroy()
        self.parent.deiconify() 

class App(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.style = ttk.Style("darkly")
        self.title("Password Manager") 
        self.geometry("1200x900")  
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
        self.account = Account(username, password) 
        res = self.users.get_account(username, password) 
        # self.create_window()  
        gui = Gui(self, self.account)   

    def create_account(self):
        username = self.username.get() 
        password = self.password.get()  
        hashed_password = self.users.hash_password(password) 
        self.account = Account(username, password)  
        self.users.add_account(username, hashed_password)  
        self.users.list_accounts() 

    def __create_widgets(self): 
        self.title_frame = ttk.Frame(self) 
        self.title_frame.pack(side = 'top', expand = True, fill = 'both')     

        self.app_title = ttk.Label(self.title_frame, text = "Password manager", font = "Calibri 32 bold" )  
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


