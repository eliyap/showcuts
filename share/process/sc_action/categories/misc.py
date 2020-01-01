from share.process.components._directory import *
from ..action import *

class encodemedia(action):
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
            '1.0',
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
        line_choose(
            'Artwork',
            'WFMetadataArtwork',
            ask_each_time=None,
            default='Choose Variable',
            options=['Choose Variable'], # NOTE revise this, 'Choose Variable' is not a real option!
        ),
    ]
    result = 'Encoded Media'

    def modify(self):
        audio_only = self.get_line('Audio Only')['class']
        if 'on' in audio_only:
            self.hide_line('Size')
        elif 'off' in audio_only:
            self.hide_line('Format')
        elif 'magic' in audio_only:
            self.hide_line('Size')
            self.hide_line('Format')

        if self.get_line('Speed')['value'] != 'Custom':
            self.hide_line('Custom Speed')
        
class trimvideo(action):
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

class ___(action):
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    category = '___'
    glyph = '___'
    result = '___'

class ___(action):
    category = '___'
    glyph = '___'
    result = '___'