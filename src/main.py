import tkinter as tk 
# from tkinter import ttk 
import ttkbootstrap as ttk 

class App(tk.Tk):
    def __init__(self):
        super().__init__() 
        self.title("Password Manager") 
        self.geometry("500x500") 
        self.__create_widgets() 

    def __create_widgets(self): 
        title_frame = ttk.Frame(self) 
        title_frame.pack(side = 'top', expand = True, fill = 'both')     

        title = ttk.Label(title_frame, text = "Bitwarden", font = "Calibri 32 bold" )  
        title.pack(side = 'top', expand = True, fill = 'y')    

        # Username and password entry frame
        up_frame =  ttk.Frame(self)
        up_frame.pack(side = 'top', fill = 'x', padx = 10, pady = 10)  

        # Username entry
        username_frame = ttk.Frame(up_frame)
        username_frame.pack(side = 'top', fill = 'x')

        username_label = ttk.Label(username_frame, text = "Username")
        username_label.pack(side = 'top', fill = 'x') 

        username_entry = ttk.Entry(username_frame, font = "Calibri 24") 
        username_entry.pack(side = 'top', fill = 'x')  

        # password entry
        password_frame = ttk.Frame(up_frame)
        password_frame.pack(side = 'top', fill = 'x') 

        password_label = ttk.Label(password_frame, text = "Master Password")
        password_label.pack(side = 'top', fill = 'x') 

        password_entry = ttk.Entry(password_frame, font = "Calibri 24")
        password_entry.pack(side = 'top', fill = 'x')   


        # Sign-in and create buttons 
        button_frame = ttk.Frame(self)
        button_frame.pack(side = 'top', fill = 'x')    

        # Sign-in button
        signIn_btn = ttk.Button(button_frame, text = "Sign In")
        signIn_btn.pack(side = 'top', fill = 'x') 
        
        
        # Create button
        create_btn = ttk.Button(button_frame, text = "Create a new account")
        create_btn.pack(side = 'top', fill = 'x')    


if __name__ == "__main__": 
    app = App() 
    app.mainloop()
    