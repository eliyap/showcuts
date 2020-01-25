from share.process.components._directory import *
from ..action import *

class encodemedia(action):
    name = 'Encode Media'
    category = 'MEDIA'
    glyph = 'QuickTime.png'
    title = [
        text('Encode'),
        magic(
            'WFMedia',
            blank_text='Media',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_toggle(
            'Audio Only',
            'WFMediaAudioOnly',
            default=False,
            ask_each_time='Ask Each Time',
        ),
        line_choose(
            'Size',
            'WFMediaSize',
            ask_each_time='Ask Each Time',
            default='Passthrough',
            options=[
                '640x480',
                '960x540',
                '1280x720',
                '1920x1080',
                'HEVC 1920x1080',
                'HEVC 3840x2160',
                'Passthrough',
            ],
        ),
        line_choose(
            'Speed',
            'WFMediaSpeed',
            ask_each_time='Ask Each Time',
            default='Normal',
            options=['0.5X','Normal','2X','Custom']
        ),
        line_pill(
            'Format',
            'WFMediaAudioFormat',
            ask_each_time='Ask Each Time',
            default='M4A',
            options=['M4A','AIFF']
        ),
        line_number(
            'Custom Speed',
            'WFMediaCustomSpeed',
            default=None,
            blank_text='1.0',
            ask_each_time='Ask Each Time',
        ),

        # METADATA
        # TODO: add a metadata collapsing tag
        line_inline(
            'Title',
            'WFMetadataTitle',
            blank_text='My Great Track',
        ),
        line_inline(
            'Artist',
            'WFMetadataArtist',
            blank_text='Nicholas Fryingpan',
        ),
        line_inline(
            'Album',
            'WFMetadataAlbum',
            blank_text='Abbey Road',
        ),
        line_inline(
            'Genre',
            'WFMetadataGenre',
            blank_text='Indie',
        ),
        line_inline(
            'Year',
            'WFMetadataYear',
            blank_text='2001',
        ),
        line_magic(
            'Artwork',
            'WFMetadataArtwork',
            blank_text='Choose Variable',
        ),
    ]
    result = 'Encoded Media'

    def modify(self):
        audio_only = self.get_line('WFMediaAudioOnly')['class']
        if 'on' in audio_only:
            self.hide_line('WFMediaSize')
        elif 'off' in audio_only:
            self.hide_line('WFMediaAudioFormat')
        elif 'magic' in audio_only:
            self.hide_line('WFMediaSize')
            self.hide_line('WFMediaAudioFormat')

        if self.get_line('WFMediaSpeed')['value'] != 'Custom':
            self.hide_line('WFMediaCustomSpeed')
        
class trimvideo(action):
    name = 'Trim Media'
    category = 'MEDIA'
    glyph = 'QuickTime.png'
    title = [
        text('Trim'),
        magic(
            'WFInputMedia',
            blank_text='Media',
            ask_each_time=None,
        ),
    ]
    result = 'Trimmed Media'

class detectlanguage(action):
    name = 'Detect Language with Microsoft'
    category = 'MICROSOFT COGNITIVE SERVICES'
    glyph = 'Language.svg'
    title = [
        text('Detect language of'),
        inline(
            'WFInput',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    result = 'Language'

class text_translate(action):
    name = 'Translate Text with Microsoft'
    languages = [
        'Detected Language',
        'Afrikaans',
        'Arabic',
        'Bangla',
        'Bosnian',
        'Bulgarian',
        'Cantonese (Traditional)',
        'Catalan',
        'Chinese Simplified',
        'Chinese Traditional',
        'Croation',
        'Czech',
        'Danish',
        'Dutch',
        'English',
        'Estonian',
        'Fijian',
        'Filipino',
        'Finnish',
        'French',
        'German',
        'Greek',
        'Haitian Creole',
        'Hebrew',
        'Hindi',
        'Hmong Daw',
        'Hungarian',
        'Icelandic',
        'Indonesian',
        'Italian',
        'Japanese',
        'Kiswahili',
        'Klingon',
        'Korean',
        'Latvian',
        'Lithuanian',
        'Malagasy',
        'Malay',
        'Maltese',
        'Maori',
        'Norwegian',
        'Persian',
        'Polish',
        'Portuguese',
        'Querétaro Otomi',
        'Romanian',
        'Russian',
        'Samoan',
        'Serbian (Cyrillic)',
        'Serbian (Latin)',
        'Slovak',
        'Slovenian',
        'Spanish',
        'Swedish',
        'Tahitian',
        'Tamil',
        'Telugu',
        'Thai',
        'Tongan',
        'Turkish',
        'Ukranian',
        'Urdu',
        'Vietnamese',
        'Welsh',
        'Yucatec Maya',
    ]
    category = 'MICROSOFT COGNITIVE SERVICES'
    title = [
        text('Translate'),
        inline(
            'WFInputText',
            blank_text='Text',
            ask_each_time='Text',
        ),
        text('from'),
        choose(
            'WFSelectedFromLanguage',
            ask_each_time='Language',
            default='Detected Language',
            options=languages,
        ),
        text('to'),
        choose(
            'WFSelectedLanguage',
            ask_each_time='To',
            default='English',
            options=languages,
        ),
    ]
    glyph = 'Language.svg'
    result = 'Translated Text'
    
class airdropdocument(action):
    name = 'Airdrop'
    category = 'AIRDROP'
    glyph = 'Airdrop.svg'
    title = [
        text('Airdrop'),
        magic(
            'WFInput',
            blank_text='Content', 
            ask_each_time=None,
        ),
    ]

class rss(action):
    name = 'Get Items from RSS Feed'
    category = 'WEB'
    glyph = 'RSS.svg'
    title = [
        text('Get'),
        counter(
            'WFRSSItemQuantity',
            'item',
            ask_each_time='Ask Each Time',
            default=10,
        ),
        text('from'),
        inline( # DETAILS UNKNOWN
            'WFRSSFeedURL',
            blank_text='UNKNOWN',
            ask_each_time='Ask Each Time',
        ), # NOTE: this seems to have default value https://www.apple.com/uk/newsroom/rss-feed.rss?
    ]
    result = 'Items from RSS Feed'

class rss_extract(action):
    name = 'Get RSS Feeds from Page'
    category = 'WEB'
    glyph = 'RSS.svg'
    title = [
        text('Get RSS feeds from'),
        magic(
            'WFURLs',
            blank_text='Page',
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'RSS Feeds from Page'

# actions below this line are not documented
class setclipboard(action):
    name = 'Copy to Clipboard'
    category = 'SHARING'
    glyph = 'Clipboard.svg'
    title = [
        text('Copy'),
        magic(
            'WFInput',
            'Content',
            ask_each_time='Ask Each Time',
        ),
        text('to clipboard'),
    ]
    lines = [
        line_toggle(
            'Local Only',
            'WFLocalOnly',
            default=False,
            ask_each_time='Ask Each Time',
        ),
        line_inline(
            'Expire At',
            'WFExpirationDate',
            blank_text='Today at 3 pm',
        ),
    ]

class getclipboard(action):
    name = 'Get Clipboard'
    category = 'SHARING'
    glyph = 'Clipboard.svg'
    result = 'Clipboard'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    name = '___'
    category = '___'
    glyph = '___'
    result = '___'
