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
        self.title("Renamer by WiktorSadowski")
        self.geometry(f"{1100}x{700}")

        #new grid layout
        #3 columns: treewiev, options and sidebar with some info
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=5)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=15)
        self.grid_rowconfigure(2, weight=1)

        #adding outlines to distinquish grid
        for col in range(1,4):
            for row in range(1,3):
                frame = ctk.CTkFrame(self, border_color="black", border_width=1)
                frame.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        #


if __name__ == "__main__":
    app = App()
    app.mainloop()