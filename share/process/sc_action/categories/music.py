from ..action import *

class _base(action):
    category = 'MUSIC'
    glyph = 'system/Music.png'

class getcurrentsong(_base):
    name = 'Get Current Song'
    result = 'Current Song'

class playmusic(_base):
    name = 'Play Music'
    pass

class pausemusic(_base):
    name = 'Play/Pause'
    glyph = 'Play-Pause.svg'
    category = 'NOW PLAYING'

class skipback(_base):
    name = 'Skip Back'
    glyph = 'Skip-Back.svg'
    category = 'NOW PLAYING'

class skipforward(_base):
    name = 'Skip Forward'
    glyph = 'Skip-Forward.svg'
    category = 'NOW PLAYING'

class exportsong(_base):
    name = 'Select Music'
    result = 'Music'

class addtoplaylist(_base):
    name = 'Add to Playlist'
    result = 'Updated Playlist'

class createplaylist(_base):
    name = 'Create Playlist'
    result = 'New Playlist'

class get_playlist(_base):
    name = 'Get Playlist'
    result = 'Playlist'

class addmusictoupnext(_base):
    name = 'Add to Up Next'

class clearupnext(_base):
    name = 'Clear Up Next'
    