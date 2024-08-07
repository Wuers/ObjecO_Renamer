import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import ttk
import os
import datetime

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #window configuration
        self.title("Renamer by Wiktor Sadowski")
        self.geometry(f"{1100}x{700}")

        #new grid layout
        #3 columns: treewiev, options and sidebar with some info
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure((0,2), weight=1)
        self.grid_rowconfigure(1, weight=10)
        
        self.label2=ctk.CTkLabel(self, text='Label2')
        self.label3=ctk.CTkLabel(self, text='Label3')

        
        #self.label2.grid(row=0, column=1)
        #self.label3.grid(row=0, column=2)

        self.title_frame = ctk.CTkFrame(self, fg_color="black")
        #self.title_frame.pack(self)
        self.title_frame.grid(row=0, columnspan=3, sticky='nsew', pady=10, padx=10)

        self.left_sidebar = ctk.CTkFrame(self, width=150, fg_color="black")
        self.left_sidebar.grid(row=1, column=0, sticky='nsew')

        self.center_frame = ctk.CTkFrame(self, width=350, fg_color="transparent")
        self.center_frame.grid(row=1, column=1, sticky='nsew', ipady=10, ipadx=10)

        self.right_frame = ctk.CTkFrame(self, width=350, fg_color="black")
        self.right_frame.grid(row=1, column=2, sticky='nsew')

        self.footer_frame = ctk.CTkFrame(self, height=40, fg_color="black")
        self.footer_frame.grid(row=2, columnspan=3, sticky='nsew', padx=10, pady=10)

        #title label
        self.title_label = ctk.CTkLabel(self.title_frame, text="Renamer", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        #center
        self.title_label2 = ctk.CTkLabel(self.center_frame, text="Center", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label2.grid(row=0, column=0, padx=10, pady=10)
        #footer
        self.footer =ctk.CTkLabel(self.footer_frame, text="Renamer by Wiktor Sadowski 2024", font=ctk.CTkFont(size=11))
        #self.footer.grid(row=0, column=0)
        self.footer.pack(expand=True)
        #treewiev

        #TO DO: SCHRINK SIZE OF TREEVIEW
        
        self.table1 = ttk.Treeview(self.center_frame, columns =('number', 'old_file_name','new_file_name','format', 'date'), show = 'headings')
        self.table1.heading('number', text = 'Number') 
        self.table1.heading('old_file_name', text = 'File name')
        self.table1.heading('new_file_name', text ='New file name')
        self.table1.heading('format', text = 'Format')
        self.table1.heading('date', text = 'Creation date')
        self.table1.grid(sticky = 'nsew')

        #add files button
        self.add_files_button = ctk.CTkButton(self.left_sidebar, text="ADD FILES")
        self.add_files_button.pack()
        #choose option button

        #frame with function options

        #

#running app
if __name__ == "__main__":
    app = App()
    app.mainloop()