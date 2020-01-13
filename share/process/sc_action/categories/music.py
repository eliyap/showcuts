from share.process.components._directory import *
from ..action import *
from ..action import *

class _base(action):
    category = 'MUSIC'
    glyph = 'system/Music.png'

class getcurrentsong(_base):
    name = 'Get Current Song'
    result = 'Current Song'

class playmusic(_base):
    name = 'Play Music'
    title = [
        text('Play'),
        music(
            'WFMediaItems',
            blank_text='Music',
            ask_each_time='Music',
        ),
    ]
    lines = [
        line_pill(
            'Shuffle',
            'WFPlayMusicActionShuffle',
            ask_each_time='Ask Each Time',
            default='', # none selected,
            options=[
                'Off',
                'Songs',
            ],
        ),
        line_pill(
            'Repeat',
            'WFPlayMusicActionRepeat',
            ask_each_time='Ask Each Time',
            default='', # none selected,
            options=[
                'None',
                'One',
                'All',
            ],
        ),
    ]
    pass

class pausemusic(_base):
    name = 'Play/Pause'
    glyph = 'Play-Pause.svg'
    category = 'NOW PLAYING'
    title = [
        choose(
            'WFPlayPauseBehavior',
            ask_each_time='Ask Each Time',
            default='Play/Pause',
            options=[
                'Play/Pause',
                'Play',
                'Pause',
            ],
        ),
        text('on'),
        choose(
            'WFMediaRoute',
            ask_each_time='Device',
            default='iPhone', # TODO: test with other devices, esp HomePods!
            options=['iPhone'],
        ),
    ]

class skipback(_base):
    name = 'Skip Back'
    glyph = 'Skip-Back.svg'
    category = 'NOW PLAYING'
    title = [
        text('Skip back to the'),
        choose(
            'WFSkipBackBehavior',
            ask_each_time='Skip To',
            default='Beginning',
            options=[
                'Beginning',
                'Previous Song',
            ],
        ),
        text('on'),
        choose(
            'WFMediaRoute',
            ask_each_time='Device',
            default='iPhone', # TODO: test with other devices, esp HomePods!
            options=['iPhone'],
        ),
    ]

class skipforward(_base):
    name = 'Skip Forward'
    glyph = 'Skip-Forward.svg'
    category = 'NOW PLAYING'

class exportsong(_base):
    name = 'Select Music'
    title = [
        text('Select music'),
    ]
    lines = [
        line_toggle(
            'Select Multiple Songs',
            'WFExportSongActionSelectMultiple',
            default = False,
            ask_each_time = 'Ask Each Time',
        )
    ]
    result = 'Music'

class addtoplaylist(_base):
    name = 'Add to Playlist'
    title = [
        text('Add'),
        magic(
            'WFInput',
            blank_text='Music',
            ask_each_time=None,
        ),
        text('to'),
        choose(
            'WFPlaylistName',
            ask_each_time='Playlist',
            default='My Music Library',
            options=['My Music Library'], # dependent on device
        ),
    ]
    result = 'Updated Playlist'

class createplaylist(_base):
    name = 'Create Playlist'
    result = 'New Playlist'

class get_playlist(_base):
    name = 'Get Playlist'
    result = 'Playlist'

class addmusictoupnext(_base):
    name = 'Add to Up Next'
    title = [
        text('Add'),
        music(
            'WFMusic',
            blank_text='Music',
            ask_each_time='Music',
        ),
        text('to'),
        choose(
            'WFWhenToPlay',
            ask_each_time='Play',
            default='Next',
            options=[
                'Next',
                'Later',
            ],
        ),
        text('of Up Next'),
    ]

class clearupnext(_base):
    name = 'Clear Up Next'
    title = [text('Clear Up Next')]
    