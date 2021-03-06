# 3M Land-It Printer User Interface
# by: Ebenezer Dadson 1/15/2020
#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):

        master.title('3M Land-It')
        master.resizable(False, False)
        master.configure(background = '#ffcc00' ) # white background

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#ffcc00')
        self.style.configure('TButton', background = '#ffcc00')
        self.style.configure('TLabel', background = '#ffcc00', font = ('Arial', 11))
        self.style.configure('Header.TLabel', background = '#ffcc00', font = ('Arial', 18, 'bold'))
        
        ## Header frame
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        # Header configuration
        self.logo = PhotoImage(file = '/home/pi/Pictures/3m.png')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2, padx = 5)
        ttk.Label(self.frame_header, text = "Land-it IoT Printer", style = 'Header.TLabel').grid(row = 0, column =1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = "Welcome! Think it, Do it, Post it, Print it! Whatever you can think up, we will Land it!").grid(row = 1, column = 1)


        ## Content frame
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        
        # Content configuration
        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        # Entry widgets 
        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        # Placements
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        # Button widgets
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, sticky = 'w')


    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = "Land-It", message = "Post-it is printing...")

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()



