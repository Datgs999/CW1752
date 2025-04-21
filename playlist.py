import tkinter as tk
from tkinter import messagebox, Listbox
import pygame
import time
import threading
import os

class PlaylistGUI:
    def __init__(self, master):
        master.configure(bg="purple")
        self.master = master

        self.playlist = []
        self.current_index = 0
        self.playing = False
        self.repeat = False

        pygame.mixer.init()

      
        self.listbox = Listbox(master, bg="black", fg="red", width=50)
        self.listbox.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

   
        tk.Button(master, text="📂 Load Playlist", command=self.load_playlist).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(master, text="▶ Play", command=self.play, bg="red", fg="white").grid(row=1, column=1, padx=5, pady=5)
        tk.Button(master, text="⏸ Pause", command=self.pause, bg="green", fg="yellow").grid(row=1, column=2, padx=5, pady=5)

        tk.Button(master, text="🔁 Resume", command=self.resume, bg="dark green", fg="white").grid(row=2, column=0, padx=5, pady=5)
        tk.Button(master, text="⏭ Next", command=self.next, bg="skyblue").grid(row=2, column=1, padx=5, pady=5)
        tk.Button(master, text="⏹ Stop", command=self.stop, fg="red").grid(row=2, column=2, padx=5, pady=5)

    
        self.status = tk.Label(master, text="Status: Ready", bg="gray", fg="white")
        self.status.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    def load_playlist(self):
        try:
            base_dir = os.path.dirname(__file__)
            filepath = os.path.join(base_dir, "List.txt")

            with open(filepath, "r", encoding="utf-8") as f:
                self.playlist = []
                self.listbox.delete(0, tk.END)
                count = 0
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) != 5:
                        continue
                    title = parts[0].strip()
                    file_path = parts[4].strip()
                    if os.path.exists(file_path):
                        self.playlist.append({"title": title, "file": file_path})
                        self.listbox.insert(tk.END, title)
                        count += 1
                    if count >= 5:
                        break
            self.status.config(text="✅ Playlist loaded.")
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi khi mở 'List.txt':\n{str(e)}")

    def play(self):
        if not self.playlist:
            self.status.config(text="⚠ No playlist loaded.")
            return
        self.playing = True
        threading.Thread(target=self._play_loop, daemon=True).start()

    def _play_loop(self):
        while self.playing and self.current_index < len(self.playlist):
            song = self.playlist[self.current_index]
            self.status.config(text=f"▶ Playing: {song['title']}")
            pygame.mixer.music.load(song["file"])
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                if not self.playing:
                    return
            self.current_index += 1
            if self.current_index >= len(self.playlist) and self.repeat:
                self.current_index = 0

    def pause(self):
        pygame.mixer.music.pause()
        self.status.config(text="⏸ Paused")

    def resume(self):
        pygame.mixer.music.unpause()
        self.status.config(text="🔁 Resumed")

    def stop(self):
        self.playing = False
        pygame.mixer.music.stop()
        self.status.config(text="⏹ Stopped")

    def next(self):
        self.current_index += 1
        pygame.mixer.music.stop()
