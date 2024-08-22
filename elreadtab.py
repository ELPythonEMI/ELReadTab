import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("El read tab")
        self.master.iconbitmap("el.ico")
        
        
        self.left_text = tk.Text(self.master, width=60, height=60)
        self.left_text.pack(side=tk.LEFT, padx=(0, 20))
        
        self.right_text = tk.Text(self.master, width=60, height=60)
        self.right_text.pack(side=tk.RIGHT, padx=(20, 0))
        
        self.small_text = tk.Text(self.master, width=60, height=38)
        self.small_text.pack()
        
        self.load_utf8_button = tk.Button(self.master, text="Load UTF-8 Text File", command=lambda: self.load_text_file("utf-8"))
        self.load_utf8_button.pack()
        
        self.load_latin1_button = tk.Button(self.master, text="Load Latin-1 Text File", command=lambda: self.load_text_file("latin-1"))
        self.load_latin1_button.pack()
        
        self.load_cp1252_button = tk.Button(self.master, text="Load CP1252 Text File", command=lambda: self.load_text_file("cp1252"))
        self.load_cp1252_button.pack()
        
        self.next_button = tk.Button(self.master, text="Next", command=self.next)
        self.next_button.pack()
        
        self.prev_button = tk.Button(self.master, text="Previous", command=self.prev)
        self.prev_button.pack()
        
        tk.Label(root,text="ELPythonEMI").pack()
        self.lines = []
        self.current_line = 0
        
    def load_text_file(self, encoding):
        file_path = filedialog.askopenfilename()
        with open(file_path, "r", encoding=encoding) as file:
            self.lines = file.readlines()
            self.current_line = 0
            self.show_lines()
    
    def next(self):
        if self.current_line + 66 < len(self.lines):
            self.current_line += 66
            self.show_lines()
    
    def prev(self):
        if self.current_line - 66 >= 0:
            self.current_line -= 66
            self.show_lines()
    
    def show_lines(self):
        self.left_text.delete("1.0", tk.END)
        self.right_text.delete("1.0", tk.END)
        self.small_text.delete("1.0", tk.END)
        for line in self.lines[self.current_line:self.current_line + 35]:
            self.left_text.insert(tk.END, ' ' + line.rstrip() + ' \n')
        for line in self.lines[self.current_line + 70:self.current_line + 103]:
            self.right_text.insert(tk.END, ' ' + line.rstrip() + ' \n')
        for line in self.lines[self.current_line + 35:self.current_line + 70]:
            self.small_text.insert(tk.END, ' ' + line.rstrip() + ' \n')

root = tk.Tk()
app = App(root)
root.mainloop()