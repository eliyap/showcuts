from ..action import *

class _base(action):
    category = 'DOCUMENTS'
    glyph = 'File.svg'

class unzip(_base):
    result = 'Files'

class makezip(_base):
    result = 'Archive'

class speaktext(_base):
    glyph = 'Volume.svg'

class avairyeditphoto(_base):
    glyph = 'Markup.svg'
    result = 'Markup Result'

class openin(_base):
    glyph = 'App.svg'

class previewdocument(_base):
    glyph = 'Quicklook.svg'

class makepdf(_base):
    glyph = 'Make-PDF.svg'
    result = 'PDF'

class print_(_base):
    glyph = 'Print.svg'

class generatebarcode(_base):
    glyph = 'QR.png'
    result = 'QR Code'

class scanbarcode(_base):
    glyph = 'QR.png'
    result = 'QR/Barcode'

class getrichtextfrommarkdown(_base):
    glyph = 'RichText.png'
    result = 'Rich Text from Markdown'

class getrichtextfromhtml(_base):
    glyph = 'RichText.png'
    result = 'Rich Text from HTML'

class gethtmlfromrichtext(_base):
    glyph = 'RichText.png'
    result = 'HTML from Rich Text'

class getmarkdownfromrichtext(_base):
    glyph = 'RichText.png'
    result = 'Markdown from Rich Text'

class dictatetext(_base):
    glyph = 'Dictate.svg'
    result = 'Dictated Text'

class getnameofemoji(_base):
    glyph = 'Emoji.svg'
    result = 'Name of Emoji'

class showdefinition(_base):
    glyph = 'Definition.svg'

class file_createfolder(_base):
    pass

class file_append(_base):
    result = 'Appended File'

class file_delete(_base):
    pass

class file_getlink(_base):
    result = 'Link to File'

class correctspelling(_base):
    glyph = 'Note.svg'
    result = 'Corrected Spelling'

class documentpicker_open(_base):
    result = 'File'

class documentpicker_save(_base):
    result = 'Saved File'