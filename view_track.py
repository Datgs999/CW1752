import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from track_library import lib  

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class TrackViewer:
    def __init__(self, parent):
        parent.configure(bg="purple")

        tk.Label(parent, text="Enter Track Number", font=("Segoe UI", 18)).grid(row=0, column=0)
        self.input_txt = tk.Entry(parent, width=5)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        list_tracks_btn = tk.Button(parent, text="List All Tracks", fg="white", bg="black", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        view_track_btn = tk.Button(parent, text="📄 View Track", fg="white", bg="black", command=self.view_track_clicked)
        view_track_btn.grid(row=1, column=1, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(parent, width=48, height=14, wrap="none", fg="red", bg="black")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(parent, width=48, height=6, wrap="none",fg="red", bg="black")
        self.track_txt.grid(row=3, column=0, columnspan=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(parent, text="", font=("Helvetica", 10), bg="purple", fg="white")
        self.status_lbl.grid(row=4, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="📋 All tracks listed.")

    def view_track_clicked(self):
     key = self.input_txt.get().strip()
     if not key.isdigit():
        set_text(self.track_txt, f"❌ '{key}' is not a valid track number.\nPlease enter a number like 1, 2, or 3.")
        self.status_lbl.configure(text=f"⚠️ Invalid input: '{key}' is not a number.")
        return

     title = lib.get_title(key)
     if title:
        artist = lib.get_artist(key)
        time = lib.get_time(key)
        listens = lib.get_formatted_listens(key)

        details = f"🎵 Title: {title}\n🎤 Artist: {artist}\n⏱ Time: {time}\n🎧 Plays: {listens}"
        set_text(self.track_txt, details)
        self.status_lbl.configure(text=f"✅ Track {key} displayed.")
     else:
        set_text(self.track_txt, f"❌ Track {key} not found.")
        self.status_lbl.configure(text=f"⚠️ Track {key} not found.")