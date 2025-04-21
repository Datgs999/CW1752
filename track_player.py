import tkinter as tk

from playlist import PlaylistGUI
from view_track import TrackViewer
from create_track_list import CreateTrackList
from update_track import UpdateTrack
import font_manager as fonts


class TrackPlayer:
    def __init__(self, window):
        self.window = window
        window.title("JukeBox")
        window.geometry("900x600")
        window.configure(bg="purple")

        fonts.configure()

        
        self.header_lbl = tk.Label(window, text="🎵 Jukebox", font=("Courier New", 24),  )
        self.header_lbl.grid(row=0, column=0, columnspan=6, sticky="ew", pady=10)

       
        self.buttons = [
            ("📄 View", self.view_tracks_clicked),
            ("🆕 New List", self.create_list_clicked),
            ("🔄 Update", self.update_tracks_clicked),
            ("▶ Playlist", self.open_playlist)
        ]

        for i, (text, command) in enumerate(self.buttons):
            btn = tk.Button(window, text=text, font=("Arial", 12), bg="black", fg="white",
                            command=command, relief="flat", borderwidth=0, padx=10, pady=10)
            btn.grid(row=1, column=i, sticky="ew")
          
            border = tk.Frame(window, bg="white", height=2)
            border.grid(row=2, column=i, sticky="ew")

        
        self.content_frame = tk.Frame(window, bg="white")
        self.content_frame.grid(row=3, column=0, columnspan=6, sticky="nsew")

      
        window.grid_rowconfigure(3, weight=1)
        window.grid_columnconfigure(5, weight=1)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def view_tracks_clicked(self):
        self.clear_content()
        TrackViewer(self.content_frame)

    def create_list_clicked(self):
        self.clear_content()
        CreateTrackList(self.content_frame)

    def update_tracks_clicked(self):
        self.clear_content()
        UpdateTrack(self.content_frame)

    def open_playlist(self):
        self.clear_content()
        PlaylistGUI(self.content_frame)


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = TrackPlayer(root)
    root.mainloop()
