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
        self.grid_columnconfigure((1,2), weight=1)
        self.grid_rowconfigure((1,2), weight=1)
       
        self.left_sidebar = ctk.CTkFrame(self, width=100, border_color="pink")
        self.left_sidebar.grid(row=1, column=1, rowspan=2)
        self.left_sidebar.grid_rowconfigure(4, weight=1)
        #adding outlines to distinquish grid
        for col in range(1,3):
            for row in range(1,3):
                frame = ctk.CTkFrame(self, border_color="black", border_width=1)
                frame.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        #title label
        self.title_label = ctk.CTkLabel(self.left_sidebar, text="Renamer (object oriented)", font=ctk.CTkFont(size=10, weight="bold"))
        self.title_label.grid(row=0, column=1, padx=10, pady=10)
        #treewiev
        #add files button
        self.add_files_button = ctk.CTkButton(self.left_sidebar)
        self.add_files_button.grid(row=2, column=1, padx=10, pady=10)
        #choose option button
        #frame with function options
        #

#running app
if __name__ == "__main__":
    app = App()
    app.mainloop()