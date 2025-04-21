import tkinter as tk
import tkinter.scrolledtext as tkst


import track_library as lib
import font_manager as fonts


def set_text(text_area, content): # set text content into text area
    text_area.delete("1.0", tk.END) # the existing content is deleted
    text_area.insert(1.0, content) # then the new one is inserted


class TrackViewer(): # the object name Trackviewer is identified
    def __init__(self, window): # use init fucntion to assign the value for window
        window.geometry("750x350")  # create GUI with(size, title)
        window.title("View Tracks")

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked) # create button to know the list of the track 
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) 

        enter_lbl = tk.Label(window, text="Enter Track Number")   # create label name enter track number 
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)   #create input box to enter track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked) # create vew track button to return output
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")  # create the scrolltext
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")  # create the output box as text
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) 

        self.list_tracks_clicked() 
    # call view track button function  
    def view_tracks_clicked(self): #import view track clicked fuction
        key = self.input_txt.get() # Get the value entered by the user from the input field
        name = lib.get_name(key) # Use the key to get the track name from the library
        if name is not None: # Check if the track exists (i.e., name is not None)
            artist = lib.get_artist(key)   # Get the artist name using the key
            rating = lib.get_rating(key)  # Get the track's rating using the key
            play_count = lib.get_play_count(key)    # Get the number of times the track has been played
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}" # Create a formatted string with track details
              
    # Display the track details in the track_txt text area
            set_text(self.track_txt, track_details) 
        else:
              # If track is not found, show a not found message
            set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="View Track button was clicked!")
    # function of list track button
    def list_tracks_clicked(self): 
        track_list = lib.list_all()  # Get the full list of tracks from the library
        set_text(self.list_txt, track_list) # Display the track list in the list_txt text area 
        self.status_lbl.configure(text="List Tracks button was clicked!")# Update the status label to show that the button was clicked

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
