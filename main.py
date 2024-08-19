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
        self.left_sidebar.grid(row=1, column=0, sticky='nsew', padx=10)

        self.center_frame = ctk.CTkFrame(self, width=350, fg_color="transparent")
        self.center_frame.grid(row=1, column=1, sticky='nsew', padx=10)

        self.right_frame = ctk.CTkFrame(self, width=350, fg_color="black")
        self.right_frame.grid(row=1, column=2, sticky='nsew', padx=10)

        self.footer_frame = ctk.CTkFrame(self, height=40, fg_color="black")
        self.footer_frame.grid(row=2, columnspan=3, sticky='nsew', padx=10, pady=10)

        #title label
        self.title_label = ctk.CTkLabel(self.title_frame, text="Renamer", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        #center
        self.center_label = ctk.CTkLabel(self.center_frame, text="Center", font=ctk.CTkFont(size=20, weight="bold"))
        self.center_label.grid(row=0, column=0, padx=10, pady=10)
        #footer
        self.footer =ctk.CTkLabel(self.footer_frame, text="Renamer by Wiktor Sadowski 2024", font=ctk.CTkFont(size=11))
        #self.footer.grid(row=0, column=0)
        self.footer.pack(expand=True)
        #treewiev
        
        self.table1 = ttk.Treeview(self.center_frame,
                                     columns =('number', 'old_file_name','new_file_name','format', 'date'),
                                     show = 'headings')
                                    
        self.table1heading = ('number', 'old_file_name','new_file_name','format', 'date')
        self.table1column = ('Number', 'File name', 'New File name', 'Format','Creation date')
        for heading, columnname in zip(self.table1heading, self.table1column):
            self.table1.heading(heading, text=columnname)
            self.table1.column(heading, anchor='center', width=120) 

        self.table1.grid(sticky = 'nsew')

        #add files button
        self.add_files_button = ctk.CTkButton(self.left_sidebar, text="ADD FILES", command=self.add_files_button)
        self.add_files_button.pack()

        #choose option button
        self.title2_label = ctk.CTkLabel(master=self.right_frame,height=20,width=100,
                           padx=10, pady=20,
                           text="Choose settings:")
        self.title2_label.pack()

        self.optionmenu_1=ctk.CTkOptionMenu(master=self.right_frame,
                                values=['Delete', 'Add','Add numbering','Find and change'],
                                command=self.option_callback)
        
        self.optionmenu_1.set('Choose option')
        self.optionmenu_1.pack()

        #inside frame with function options
        self.outer_option_frame=ctk.CTkFrame(master=self.right_frame)
        self.outer_option_frame.pack(pady=20, padx=20, fill="both", expand=True)
        #
        self.option_frame=ctk.CTkFrame(master=self.outer_option_frame)
        self.option_frame.pack()


    def add_files_button(self):
            #1 selecting files, returns list of files directories
        global file_paths_list
        file_paths_list = fd.askopenfilenames(initialdir='E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES')
        #loop that removes all files from table:
        for item in self.table1.get_children():
            self.table1.delete(item)
            
        global name_format_list
        def f_nested_files_list(file_path_list):
            #returns nested list of [[name1,format1,date1,file1_path](...)]
            #global format_index
            global fetched_list
            fetched_list = []
            for file in file_path_list:
                name = os.path.basename(file)
                name_without_exntension = os.path.splitext(name)[0]
                format = os.path.splitext(name)[1][1:]
                creation_time = os.path.getctime(file)
                creation_date = datetime.datetime.fromtimestamp(creation_time)
                formated_creation_date = creation_date.strftime("%Y-%m-%d %H:%M")

                #item is a tuple - file information.
                item = [name_without_exntension, format, formated_creation_date, file]
                fetched_list.append(item)

                # adding info to table:    
            for index,file in enumerate(fetched_list, start=1):
                file_name, format, date, full_path = file
                data = [index, file_name,'-', format, date]
                self.table1.insert(parent='', index='end', values=data)
            return fetched_list
        
        name_format_list=f_nested_files_list(file_paths_list)
        ##delete this
        print(f"name format list to: {name_format_list}")
        return name_format_list

    def validate_insert_if_int(self,V):
        #function to validate if inserted character is int
        if V == "" or V.isdigit():
            return True
        else:
            return False

    def get_delete_value(self):
        #function that return int value from delete_entry
        global delete_entry
        value = delete_entry.get()
        if value.isdigit():
            return int(value)
        else:
            print ("Please insert only value, not string etc")
            return None
    
    def delete_preview(self): 
        num_chars = self.get_delete_value()
        if num_chars is not None:
            global position
            position = radio_var.get()
            global fetched_list
            new_fetched_list, old_and_new_paths = self.delete_from_filenames(num_chars, position, fetched_list)
            for old, new in old_and_new_paths:
                print(f"OLD: {old}")
                print(f"NEW: {new}")
                print("-----")
            self.update_table(new_fetched_list)
        else:
            print ("num_chars is bugged. Current value:", num_chars)
        global confirmation_label
        if 'confirmation_label' in globals() and confirmation_label.winfo_exists():
            confirmation_label.destroy()

    def delete_save(self):
        # call delete_from_filenames to get old and new file paths
        num_chars = self.get_delete_value()
        position = radio_var.get()
        global fetched_list
        
        modified_list, old_and_new_path = self.delete_from_filenames(num_chars, position, fetched_list)
        for old_path, new_path in old_and_new_path:
            try:
                os.rename(old_path, new_path)
            except OSError as e:
                print(f"Error renaming {old_path} to {new_path}: {e}")

        # update table with new names
        self.update_table(modified_list)

        #confirmation label:
        global confirmation_label
        confirmation_label = ctk.CTkLabel(
        master = self.right_frame,
        text = 'Changes saved!'
        )
        confirmation_label.pack()
        #deleting elements from list
        for item in self.table1.get_children():
            self.table1.delete(item)

    def add_preview(self): 
        global add_string_entry
        custom_string = add_string_entry.get()
        position = int(add_position_entry.get())

        if custom_string is not None and position is not None:
            global fetched_list
            new_fetched_list, old_and_new_paths = self.add_to_filenames(custom_string, position, fetched_list)
            for old, new in old_and_new_paths:
                print(f"OLD: {old}")
                print(f"NEW: {new}")
                print("-----")
            self.update_table(new_fetched_list)
        else:
            print ("add_string is bugged. Current value:", position)
        global confirmation_label
        if 'confirmation_label' in globals() and confirmation_label.winfo_exists():
            confirmation_label.destroy()

    def add_save(self):
        # call delete_from_filenames to get old and new file paths
        custom_string = add_string_entry.get()
        position = int(add_position_entry.get())
        global fetched_list
        
        modified_list, old_and_new_path = self.add_to_filenames(custom_string, position, fetched_list)
        for old_path, new_path in old_and_new_path:
            try:
                os.rename(old_path, new_path)
            except OSError as e:
                print(f"Error renaming {old_path} to {new_path}: {e}")

        # update table with new names
        self.update_table(modified_list)

        #confirmation label:
        global confirmation_label
        confirmation_label = ctk.CTkLabel(
        master = self.right_frame,
        text = 'Changes saved!'
        )
        confirmation_label.pack()
        #deleting elements from list
        for item in self.table1.get_children():
            self.table1.delete(item)

    def option_callback(self,choice):
        #function that displays elements needed for the function that has been selected

        self.clear_option_frame()
        
        if choice == "Delete":

            global radio_var
            radio_var = ctk.StringVar(value="")
            self.option_frame = ctk.CTkFrame(master=self.outer_option_frame)
        
            radio_1 = ctk.CTkRadioButton(master=self.option_frame, text="At the beginning", variable=radio_var, value="beginning")
            radio_1.grid()

            radio_2 = ctk.CTkRadioButton(master=self.option_frame, text="From end", variable=radio_var, value="end")
            radio_2.grid()

            #entry to insert number of characters thats going to be deleted:
            validate_cmd=self.option_frame.register(self.validate_insert_if_int)

            #entry to insert number:
            global delete_entry
            delete_entry = ctk.CTkEntry(
                master=self.option_frame,
                placeholder_text="insert number of character to be deleted",
                width=250,
                validate="key",
                validatecommand=(validate_cmd, '%P')
                )       
            delete_entry.grid()

            #button to send value and preview:
            self.func_d_preview_button = ctk.CTkButton(
                master=self.option_frame,
                text="Preview",
                command=self.delete_preview
            )
            self.func_d_preview_button.grid()


            #button to save changes to files
            self.func_d_save_button = ctk.CTkButton(
                master=self.option_frame,
                text="SAVE CHANGES",
                command=self.delete_save
            )
            self.func_d_save_button.grid()
            
        elif choice == "Add":
            print(f"it works! almost")
            self.option_frame = ctk.CTkFrame(master=self.outer_option_frame)

            #entry to insert number of characters thats going to be deleted:
            validate_cmd=self.option_frame.register(self.validate_insert_if_int)

            #entry to insert added string:
            global add_string_entry
            global add_position_entry
            add_string_entry = ctk.CTkEntry(
                master=self.option_frame,
                placeholder_text="insert text that you want to add",
                width=250)
            add_string_entry.grid()

            add_position_entry = ctk.CTkEntry(
                master=self.option_frame,
                placeholder_text="insert position where to add your custom text",
                width=250)
            add_position_entry.grid()

            #button to send value and preview:
            self.func_a_preview_button = ctk.CTkButton(
                master=self.option_frame,
                text="Preview",
                command=self.add_preview
            )
            self.func_a_preview_button.grid()

            #button to save changes to files
            self.func_a_save_button = ctk.CTkButton(
                master=self.option_frame,
                text="SAVE CHANGES",
                command=self.add_save
            )
            self.func_a_save_button.grid()

        elif choice == "Add numbering":
            
            self.option_frame = ctk.CTkFrame(master=self.outer_option_frame)
            self.option_frame.grid()
            custom_label = ctk.CTkLabel(master=self.option_frame, text='To be implemented in the future')
            custom_label.grid()
             
        elif choice == "Find and change":
            self.option_frame = ctk.CTkFrame(master=self.outer_option_frame)
            self.option_frame.grid()
            custom_label = ctk.CTkLabel(master=self.option_frame, text='To be implemented in the future')
            custom_label.grid()
            
        self.option_frame.pack()

    def delete_from_filenames(self, num_chars, position, list):
        
    #function that returns two list: new, modified and list with old and new paths
        modified_list = []
        old_and_new_path = []
        for item in list:
            try:
                name, format, date, full_path = item
            except ValueError as e:
                print ("error is: ", e)
                print (f"error when unpacking tuple 'item'. problematic element: {item}")
                continue
            if position == "beginning":
                old_name = name
                new_name = name[num_chars:]
            elif position == "end":
                old_name = name
                new_name = name[:-num_chars] if len(name) > num_chars else ""
            else:
                new_name = name

            old_path = full_path
            #new_path = os.path.join(os.path.dirname(full_path), f"{new_name}.{format}")
            new_path = os.path.normpath(os.path.join(os.path.dirname(full_path), f"{new_name}.{format}"))

            modified_list.append([new_name, old_name, format, date, new_path])
            old_and_new_path.append((old_path, new_path))

        return modified_list, old_and_new_path
    
    def add_to_filenames(self, string_to_add, string_position, list):
        
    #function that returns two list: new (modified) and list with old and new paths
        modified_list = []
        old_and_new_path = []
        
        for item in list:
            try:
                name, format, date, full_path = item
            except ValueError as e:
                print ("error is: ", e)
                print (f"error when unpacking tuple 'item'. problematic element: {item}")
                continue
            old_name = name
            #new_name = item[0:2]+custom_string+item[2:]
            new_name = name[0:string_position-1]+string_to_add+name[string_position-1:]
            old_path = full_path
            new_path = os.path.normpath(os.path.join(os.path.dirname(full_path), f"{new_name}.{format}"))

            modified_list.append([new_name, old_name, format, date, new_path])
            old_and_new_path.append((old_path, new_path))

        return modified_list, old_and_new_path

    def update_table(self, new_list):
    #updates table
        #delete current preview
        for item in self.table1.get_children():
            self.table1.delete(item)
        #add new preview
        for index, item in enumerate(new_list, start=1):
            name, old_name, format, date, full_path = item
            self.table1.insert('', 'end', values=(index, old_name, name, format, date))

    def clear_option_frame(self):
        #clears option frame
        if self.option_frame is not None:
            self.option_frame.destroy()
            self.option_frame = None
        return None


if __name__ == "__main__":
    app = App()
    app.mainloop()