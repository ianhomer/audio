from pathlib import Path
from unittest import TestCase

from audioarchivist.song import Song
from audioarchivist.tests.storage import Storage

storage = Storage()

class TestSongMove(TestCase):
    def test_song_move(self):
        relativeFilename = "samples/Move - samples - Purpley.mp3"
        filename = storage.tmp("mp3", "meta-move/from/" + relativeFilename)
        song = Song(filename)
        source = Path(filename)
        self.assertTrue(source.exists())
        song.move("to")
        self.assertFalse(source.exists())
        destination = Path(storage.tmpFilename("meta-move/to/" + relativeFilename))
        self.assertTrue(destination.exists())
        destination.unlink()
        storage.tmpRemove("meta-move/from/samples")
        storage.tmpRemove("meta-move/from")
        storage.tmpRemove("meta-move/to/samples")
        storage.tmpRemove("meta-move/to")
