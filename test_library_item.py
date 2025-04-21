import pytest
from library_item import LibraryItem

def test_info_format():
    item = LibraryItem("Song A", "Artist B", "03:45", 5000)
    assert item.info() == "Song A - Artist B (03:45) [5K listens]"

def test_listens_conversion():
    item = LibraryItem("Track", "Band", "04:10", "1000000")
    assert item.listens == 1000000
    assert "1M" in item.info()

def test_invalid_listens_raises():
    with pytest.raises(ValueError):
        LibraryItem("Wrong", "Input", "04:20", "four")
