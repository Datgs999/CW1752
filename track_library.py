from library_item import LibraryItem
from playlist import PlaylistGUI

class Library:
    def __init__(self):
        self.library = {
            1: LibraryItem("brother louie", "Modern Talking", "3:28", 290000, "music/brother louie.mp3"),
            2: LibraryItem("Hello", "Lionel Richie", "5:26", 9000000, "music/Hello.mp3"),
            3: LibraryItem("River Flow in you", "Yiruma", "3:08", 5500000, "music/river flow in you.mp3"),
            4: LibraryItem("Holding Out Of A Hero", "Bonnie Tyler", "3:58", 5000000, "music/hero.mp3"),
            5: LibraryItem("No Face, No Name, No Number", "Modern Talking", "4:45", 60000, "music/ face,name,number.mp3"),
        }

    def list_all(self):
        output = ""
        for key, item in self.library.items():
            output += f"{key} {item.info()}\n"
        return output

    def get_title(self, key):
        try:
            return self.library[int(key)].title
        except (KeyError, ValueError):
            return None 

    def get_artist(self, key):
        try:
            return self.library[int(key)].artist
        except (KeyError, ValueError):
            return None

    def get_listens(self, key):
        try:
            return self.library[int(key)].listens
        except (KeyError, ValueError):
            return -1

    def get_formatted_listens(self, key):
        """🆕 Thêm hàm này nếu bạn muốn lấy chuỗi định dạng sẵn: 29M, 60K..."""
        try:
            return self.library[int(key)]._format_listens()
        except (KeyError, ValueError):
            return "?"

    def set_listens(self, key, listens):
        try:
            self.library[int(key)].listens = int(listens)
        except (KeyError, ValueError):
            pass

    def get_time(self, key):
        try:
            return self.library[int(key)].time
        except (KeyError, ValueError):
            return None

    def increment_listens(self, key):
        try:
            self.library[int(key)].listens += 1
        except (KeyError, ValueError):
            pass

# Tạo đối tượng lib từ class Library
lib = Library()
