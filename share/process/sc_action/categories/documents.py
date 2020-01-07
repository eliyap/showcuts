from ..action import *

class _base(action):
    category = 'DOCUMENTS'
    glyph = 'File.svg'

class unzip(_base):
    name = 'Extract Archive'
    result = 'Files'

class makezip(_base):
    name = 'Make Archive'
    result = 'Archive'

class speaktext(_base):
    name = 'Speak Text'
    glyph = 'Volume.svg'

class avairyeditphoto(_base):
    name = 'Markup'
    glyph = 'Markup.svg'
    result = 'Markup Result'

class openin(_base):
    name = 'Open In...'
    glyph = 'App.svg'

class previewdocument(_base):
    name = 'Quick Look'
    glyph = 'Quicklook.svg'

class makepdf(_base):
    name = 'Make PDF'
    glyph = 'Make-PDF.svg'
    result = 'PDF'

class print_(_base):
    name = 'Print'
    glyph = 'Print.svg'

class generatebarcode(_base):
    name = 'Generate QR Code'
    glyph = 'QR.png'
    result = 'QR Code'

class scanbarcode(_base):
    name = 'Scan QR/Barcode'
    glyph = 'QR.png'
    result = 'QR/Barcode'

class getrichtextfrommarkdown(_base):
    name = 'Make Rich Text from Markdown'
    glyph = 'RichText.png'
    result = 'Rich Text from Markdown'

class getrichtextfromhtml(_base):
    name = 'Make Rich Text from HTML'
    glyph = 'RichText.png'
    result = 'Rich Text from HTML'

class gethtmlfromrichtext(_base):
    name = 'Make HTML from Rich Text'
    glyph = 'RichText.png'
    result = 'HTML from Rich Text'

class getmarkdownfromrichtext(_base):
    name = 'Make Markdown from Rich Text'
    glyph = 'RichText.png'
    result = 'Markdown from Rich Text'

class dictatetext(_base):
    name = 'Dictate Text'
    glyph = 'Dictate.svg'
    result = 'Dictated Text'

class getnameofemoji(_base):
    name = 'Get Name of Emoji'
    glyph = 'Emoji.svg'
    result = 'Name of Emoji'

class showdefinition(_base):
    name = 'Show Definition'
    glyph = 'Definition.svg'

class file_createfolder(_base):
    name = 'Create Folder'

class file_append(_base):
    name = 'Append to File'
    result = 'Appended File'

class file_delete(_base):
    name = 'Delete Files'

class file_getlink(_base):
    name = 'Get Link to File'
    result = 'Link to File'

class correctspelling(_base):
    name = 'Correct Spelling'
    glyph = 'Note.svg'
    result = 'Corrected Spelling'

class documentpicker_open(_base):
    name = 'Get File'
    result = 'File'

class documentpicker_save(_base):
    name = 'Save File'
    result = 'Saved File'