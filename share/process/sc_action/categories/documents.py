from share.process.components._directory import *
from ..action import *

class _base(action):
    category = 'DOCUMENTS'
    glyph = 'File.svg'

class unzip(_base):
    name = 'Extract Archive'
    title = [
        text('Extract'),
        magic(
            'WFArchive',
            blank_text='Archive',
            ask_each_time=None,
        ),
    ]
    result = 'Files'

class makezip(_base):
    name = 'Make Archive'
    title = [
        text('Make'),
        choose(
            'WFArchiveFormat',
            ask_each_time='Format',
            default='.zip',
            options=[
                '.zip',
                '.tar.gz',
                '.tar.bz2',
                '.tar.xz',
                '.tar',
                '.gz',
                '.cpio',
                '.iso',
            ],
        ),
        text('archive from'),
        magic(
            'WFInput',
            blank_text='Input',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_inline(
            'Archive Name',
            'WFZIPName',
            blank_text='optional',
        ),
    ]
    result = 'Archive'

    def modify(self):
        fmt = self.get_title('WFArchiveFormat')['value']
        if fmt[0] != '.' and fmt != 'Format': # check not  Ask_Each_Time
            self.get_title('WFArchiveFormat')['value'] = f'.{fmt}'

class speaktext(_base):
    name = 'Speak Text'
    glyph = 'Volume.svg'

class avairyeditphoto(_base):
    name = 'Markup'
    glyph = 'Markup.svg'
    title = [
        text('Mark up'),
        magic(
            'WFDocument',
            blank_text='Document',
            ask_each_time=None,
        ),
    ]
    result = 'Markup Result'

class openin(_base):
    name = 'Open In...'
    glyph = 'App.svg'
    title = [
        text('Open'),
        magic(
            'WFInput',
            blank_text='File',
            ask_each_time=None,
        ),
        text('in'),
        magic(
            'WFOpenInAppIdentifier',
            blank_text='Choose',
            ask_each_time=None,
        ), # possibly should be a `choose`, with a list of our supported apps
    ]
    lines = [
        line_toggle(
            'Show Open In Menu',
            'WFOpenInAskWhenRun',
            default=True,
            ask_each_time='Ask Each Time',
        ),
        line_magic(
            'File',
            'WFInput',
            blank_text='File',
        ),
    ]

    def modify(self):
        import logging # DEBUG
        logging.error(self.get_line('WFOpenInAskWhenRun'))
        if 'on' in self.get_line('WFOpenInAskWhenRun')['class']:
            self.hide_text('in')
            self.hide_title('WFOpenInAppIdentifier')
            
        if self.get_line('WFOpenInAskWhenRun')['value'] == 'Ask Each Time':
            self.title = text('Open In...').to_html()
        else:
            self.hide_line('WFInput')


class previewdocument(_base):
    name = 'Quick Look'
    glyph = 'Quicklook.svg'
    title = [
        text('Show'),
        magic(
            'WFInput',
            blank_text='Input',
            ask_each_time=None,
        ),
        text('in Quick Look'),
    ]

class makepdf(_base):
    name = 'Make PDF'
    glyph = 'Make-PDF.svg'
    title = [
        text('Make PDF from'),
        magic(
            'WFInput',
            blank_text='Input',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_toggle(
            'Include Margin',
            'WFPDFIncludeMargin',
            default=False,
            ask_each_time='Ask Each Time',
        ),
        line_choose(
            'Include',
            'WFPDFIncludedPages',
            ask_each_time='Ask Each Time',
            default='All Pages',
            options=[
                'All Pages',
                'Single Page',
                'Page Range',
            ],
        ),
        line_number(
            'Page No.',
            'WFPDFSinglePage',
            default=None,
            blank_text='1',
            ask_each_time='Ask Each Time',
        ),
        line_number(
            'Start Page No.',
            'WFPDFPageRangeStart',
            default=None,
            blank_text='1',
            ask_each_time='Ask Each Time',
        ),
        line_number(
            'End Page No.',
            'WFPDFPageRangeEnd',
            default=None,
            blank_text='3',
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'PDF'

    def modify(self):
        {
            'Ask Each Time': lambda:[
                self.hide_line('WFPDFSinglePage'),
                self.hide_line('WFPDFPageRangeStart'),
                self.hide_line('WFPDFPageRangeEnd'),
            ],
            'All Pages': lambda:[
                self.hide_line('WFPDFSinglePage'),
                self.hide_line('WFPDFPageRangeStart'),
                self.hide_line('WFPDFPageRangeEnd'),
            ],
            'Single Page': lambda:[
                self.hide_line('WFPDFPageRangeStart'),
                self.hide_line('WFPDFPageRangeEnd'),
            ],
            'Page Range': lambda:[
                self.hide_line('WFPDFSinglePage'),
            ],
        }.get(
            self.get_line('WFPDFIncludedPages')['value'],
            lambda: [],
        )()    

class print_(_base):
    name = 'Print'
    glyph = 'Print.svg'
    title = [
        text('Print'),
        magic(
            'WFInput',
            blank_text='Input',
            ask_each_time=None,
        ),
    ]

class generatebarcode(_base):
    name = 'Generate QR Code'
    glyph = 'QR.png'
    title = [
        text('Generate QR code from'),
        inline(
            'WFText',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    lines = [
        line_choose(
            'Error Correction',
            'WFQRErrorCorrectionLevel',
            ask_each_time='Ask Each Time',
            default='Medium',
            options=[
                'Low',
                'Medium',
                'Quartile',
                'High',
            ],
        ),
    ]
    result = 'QR Code'

class scanbarcode(_base):
    name = 'Scan QR/Barcode'
    glyph = 'QR.png'
    title = [text('Scan QR/Barcode')]
    result = 'QR/Barcode'

class getrichtextfrommarkdown(_base):
    name = 'Make Rich Text from Markdown'
    glyph = 'RichText.png'
    title = [
        text('Make rich text from'),
        magic(
            'WFInput',
            blank_text='Markdown Text',
            ask_each_time=None,
        ),
    ]
    result = 'Rich Text from Markdown'

class getrichtextfromhtml(_base):
    name = 'Make Rich Text from HTML'
    glyph = 'RichText.png'
    title=[
        text('Make rich text from'),
        magic(
            'WFHTML',
            blank_text='HTML',
            ask_each_time=None,
        ),
    ]
    result = 'Rich Text from HTML'

class gethtmlfromrichtext(_base):
    name = 'Make HTML from Rich Text'
    glyph = 'RichText.png'
    title=[
        text('Make HTML from'),
        magic(
            'WFHTML',
            blank_text='Rich Text',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_toggle(
            'Make Full Document',
            'WFMakeFullDocument',
            default=False,
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'HTML from Rich Text'

class getmarkdownfromrichtext(_base):
    name = 'Make Markdown from Rich Text'
    glyph = 'RichText.png'
    title = [
        text('Make Markdown from'),
        magic(
            'WFInput',
            blank_text='Rich Text',
            ask_each_time=None,
        ),
    ]
    result = 'Markdown from Rich Text'

class dictatetext(_base):
    name = 'Dictate Text'
    glyph = 'Dictate.svg'
    result = 'Dictated Text'

class getnameofemoji(_base):
    name = 'Get Name of Emoji'
    glyph = 'Emoji.svg'
    title = [
        text('Get name of emoji in'),
        inline(
            'WFInput',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    result = 'Name of Emoji'

class showdefinition(_base):
    name = 'Show Definition'
    glyph = 'Definition.svg'
    title = [
        text('Show definition of'),
        inline(
            'Word',
            blank_text='word',
            ask_each_time='Text',
        ),
    ]

class file_createfolder(_base):
    name = 'Create Folder'

class file_append(_base):
    name = 'Append to File'
    title = [
        choose(
            'WFAppendFileWriteMode',
            ask_each_time='Mode',
            default='Append',
            options=[
                'Append',
                'Prepend',
            ],
        ),
        inline(
            'WFInput',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    lines = [
        line_choose(
            'Service',
            'WFFileStorageService',
            ask_each_time=None,
            default='iCloud Drive',
            options=[
                'iCloud Drive',
                'Dropbox',
            ],
        ),
        line_inline(
            'File Path',
            'WFFilePath',
            blank_text='/example.txt',
            leftify=True,
        ),
        line_toggle(
            'Make New Line',
            'WFAppendOnNewLine',
            default=True,
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Appended File'

class file_delete(_base):
    name = 'Delete Files'
    title = [
        text('Delete'),
        magic(
            'WFInput', 
            blank_text='Files',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_toggle(
            'Confirm Before Deleting',
            'WFDeleteFileConfirmDeletion',
            default=True,
            ask_each_time='Ask Each Time',
        ),
    ]

class file_getlink(_base):
    name = 'Get Link to File'
    title = [
        text('Get link to'),
        magic(
            'WFFile',
            blank_text='File',
            ask_each_time=None,
        ),
    ]
    result = 'Link to File'

class correctspelling(_base):
    name = 'Correct Spelling'
    glyph = 'Note.svg'
    title = [
        text('Correct spelling of'),
        list_inline(
            'text',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    result = 'Corrected Spelling'

class documentpicker_open(_base):
    name = 'Get File'
    title = [
        text('Get File'),
    ]
    lines = [
        line_choose(
            'Service',
            'WFFileStorageService',
            ask_each_time=None,
            default='iCloud Drive',
            options=[
                'iCloud Drive',
                'Dropbox',
            ],
        ),
        line_toggle(
            'Show Document Picker',
            'WFShowFilePicker',
            default=True,
            ask_each_time='Ask Each Time',
        ),
        line_inline(
            'File Path',
            'WFFilePath',
            blank_text='/example.txt',
            leftify=True,
        ),
        line_toggle(
            'Error If Not Found',
            'WFFileErrorIfNotFound',
            default=True,
            ask_each_time='Ask Each Time',
        ),
        line_inline(
            'Initial Path',
            'WFGetFileInitialDirectoryPath',
            blank_text='optional',
            leftify=True,
        ),
    ]
    result = 'File'

class documentpicker_save(_base):
    name = 'Save File'
    title = [
        text('Save'),
        magic(
            'WFInput',
            blank_text='File',
            ask_each_time=None,
        ),
    ]
    lines = [
        line_choose(
            'Service',
            'WFFileStorageService',
            ask_each_time=None,
            default='iCloud Drive',
            options=[
                'iCloud Drive',
                'Dropbox',
            ],
        ),
        line_toggle(
            'Ask Where to Save',
            'WFAskWhereToSave',
            default=True,
            ask_each_time='Ask Each Time',
        ),
        line_inline( # NOTE: text changes depending on service chosen!
            'Destination Path',
            'WFFileDestinationPath',
            'Text',
            leftify=True,
        ),
        line_toggle(
            'Overwrite If File Exists',
            'WFSaveFileOverwrite',
            default=False,
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Saved File'