from ..action import *

class _base(action):
    category = 'DOCUMENTS'
    glyph = 'File.svg'

class unzip(_base):
    name = '___'
    result = 'Files'

class makezip(_base):
    name = '___'
    result = 'Archive'

class speaktext(_base):
    name = '___'
    glyph = 'Volume.svg'

class avairyeditphoto(_base):
    name = '___'
    glyph = 'Markup.svg'
    result = 'Markup Result'

class openin(_base):
    name = '___'
    glyph = 'App.svg'

class previewdocument(_base):
    name = '___'
    glyph = 'Quicklook.svg'

class makepdf(_base):
    name = '___'
    glyph = 'Make-PDF.svg'
    result = 'PDF'

class print_(_base):
    name = '___'
    glyph = 'Print.svg'

class generatebarcode(_base):
    name = '___'
    glyph = 'QR.png'
    result = 'QR Code'

class scanbarcode(_base):
    name = '___'
    glyph = 'QR.png'
    result = 'QR/Barcode'

class getrichtextfrommarkdown(_base):
    name = '___'
    glyph = 'RichText.png'
    result = 'Rich Text from Markdown'

class getrichtextfromhtml(_base):
    name = '___'
    glyph = 'RichText.png'
    result = 'Rich Text from HTML'

class gethtmlfromrichtext(_base):
    name = '___'
    glyph = 'RichText.png'
    result = 'HTML from Rich Text'

class getmarkdownfromrichtext(_base):
    name = '___'
    glyph = 'RichText.png'
    result = 'Markdown from Rich Text'

class dictatetext(_base):
    name = '___'
    glyph = 'Dictate.svg'
    result = 'Dictated Text'

class getnameofemoji(_base):
    name = '___'
    glyph = 'Emoji.svg'
    result = 'Name of Emoji'

class showdefinition(_base):
    name = '___'
    glyph = 'Definition.svg'

class file_createfolder(_base):
    name = '___'

class file_append(_base):
    name = '___'
    result = 'Appended File'

class file_delete(_base):
    name = '___'

class file_getlink(_base):
    name = '___'
    result = 'Link to File'

class correctspelling(_base):
    name = '___'
    glyph = 'Note.svg'
    result = 'Corrected Spelling'

class documentpicker_open(_base):
    name = '___'
    result = 'File'

class documentpicker_save(_base):
    name = '___'
    result = 'Saved File'