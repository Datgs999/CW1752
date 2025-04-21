class LibraryItem:
    def __init__(self, title, artist, time, listens=0, file_path=None):
        self.title = title
        self.artist = artist
        self.time = time
        self.file_path = file_path
        self.listens = int(listens)

    def info(self):
        return f"{self.title} - {self.artist} ({self.time}) [{self._format_listens()} listens]"

    def _format_listens(self):
        if self.listens >= 1_000_000:
            return f"{self.listens // 1_000_000}M"
        elif self.listens >= 1_000:
            return f"{self.listens // 1_000}K"
        else:
            return str(self.listens)


