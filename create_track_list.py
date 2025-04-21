import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox


  

class CreateTrackList:
    def __init__(self, parent):
        parent.configure(bg="purple")

        # Title
        tk.Label(parent, text="Song List", font=("Arial", 14)).grid(row=0, column=0, columnspan=3, pady=10)

        # Input fields
        tk.Label(parent, text="Title:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.Title = tk.Entry(parent)
        self.Title.grid(row=1, column=1, columnspan=2, sticky="ew")

        tk.Label(parent, text="Artist", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.Artist = tk.Entry(parent)
        self.Artist.grid(row=2, column=1, columnspan=2, sticky="ew")

        tk.Label(parent, text="Time:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.Time = tk.Entry(parent)
        self.Time.grid(row=3, column=1, columnspan=2, sticky="ew")

        tk.Label(parent, text="Listens:", font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.Listens = tk.Entry(parent)
        self.Listens.grid(row=4, column=1, columnspan=2, sticky="ew")

        # Action buttons
        tk.Button(parent, text="+ Add",fg= "white", bg= "black",command=self.add_click).grid(row=5, column=0, pady=5)
        tk.Button(parent, text="Delete",fg= "white", bg= "black", command=self.delete_click).grid(row=5, column=1, pady=5)
     

        

        # List headers
        tk.Label(parent, text="Title", font=("Arial", 9)).grid(row=7, column=0, pady=5)
        tk.Label(parent, text="Artist", font=("Arial", 9)).grid(row=7, column=1, pady=5)
        tk.Label(parent, text="Time", font=("Arial", 9)).grid(row=7, column=2, pady=5)
        tk.Label(parent, text="Listens", font=("Arial", 9)).grid(row=7, column=3, pady=5)

        # Display area
        self.text_area = tkst.ScrolledText(parent, font=("Helvetica", 12), height=10, width=70, fg="red", bg="black")
        self.text_area.grid(row=8, column=0, columnspan=4, pady=10, sticky="ew")

    def add_click(self):
        title = self.Title.get()
        artist = self.Artist.get()
        time = self.Time.get()
        listens = self.Listens.get()

        if title and artist and time and listens:
            line = f"{title}\t{artist}\t{time}\t{listens}\n"
            self.text_area.insert(tk.END, line)
            self.clear_inputs()
        else:
            messagebox.showwarning("Missing info", "Please fill in all fields")

    
    def delete_click(self):
        self.text_area.delete("1.0", tk.END)

 

  

    def clear_inputs(self):
        self.Title.delete(0, tk.END)
        self.Artist.delete(0, tk.END)
        self.Time.delete(0, tk.END)
        self.Listens.delete(0, tk.END)

