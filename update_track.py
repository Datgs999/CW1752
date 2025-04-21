import tkinter as tk
from tkinter import messagebox



class UpdateTrack:
    def __init__(self, parent):
        parent.configure(bg="purple")
       

        # Label and Entry for Title
        label1 = tk.Label(parent, text="Title", font=("Arial", 14))
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.title_entry = tk.Entry(parent)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for Artist
        label2 = tk.Label(parent, text="Artist", font=("Arial", 14))
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.artist_entry = tk.Entry(parent)
        self.artist_entry.grid(row=1, column=1, padx=10, pady=10)

        # Label and Entry for Listens
        label3 = tk.Label(parent, text="Listens", font=("Arial", 14))
        label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.listens_entry = tk.Entry(parent)
        self.listens_entry.grid(row=2, column=1, padx=10, pady=10)

        # Label and Entry for Time
        label4 = tk.Label(parent, text="Time", font=("Arial", 14))
        label4.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.time_entry = tk.Entry(parent)
        self.time_entry.grid(row=3, column=1, padx=10, pady=10)

        # Update button
        update_button = tk.Button(parent, text="Update", font=("Arial", 14),fg= "white",bg="black", command=self.update_click)
        update_button.grid(row=4, column=0, columnspan=2, pady=20)

    def update_click(self):
        title = self.title_entry.get()
        artist = self.artist_entry.get()
        listens = self.listens_entry.get()
        time = self.time_entry.get()

        if not title or not artist or not listens or not time:
            messagebox.showinfo("Warning", "Please fill all fields")
        else:
            self.update_track(title, artist, listens, time)

    def update_track(self, title, artist, listens, time):
        try:
            print("Updating track...")
            print(f"Title: {title}")
            print(f"Artist: {artist}")
            print(f"Listens: {listens}")
            print(f"Time: {time}")
            messagebox.showinfo("Notice", "Update successful")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")





