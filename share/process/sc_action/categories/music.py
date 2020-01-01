from ..action import *

class _base(action):
    category = 'MUSIC'
    glyph = 'system/Music.png'

class getcurrentsong(_base):
    result = 'Current Song'

class playmusic(_base):
    pass

class pausemusic(_base):
    glyph = 'Play-Pause.svg'
    category = 'NOW PLAYING'

class skipback(_base):
    glyph = 'Skip-Back.svg'
    category = 'NOW PLAYING'

class skipforward(_base):
    glyph = 'Skip-Forward.svg'
    category = 'NOW PLAYING'

class exportsong(_base):
    result = 'Music'

class addtoplaylist(_base):
    result = 'Updated Playlist'

class createplaylist(_base):
    result = 'New Playlist'

class get_playlist(_base):
    result = 'Playlist'

class addmusictoupnext(_base):
    pass

class clearupnext(_base):
    def to_django(self, params):
        pass