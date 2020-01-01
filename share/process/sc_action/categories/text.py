from ..action import *

class _base(action):
    category = 'TEXT'
    glyph = 'Note.svg'

class gettext(_base):
    result = 'Text'

class text_replace(_base):
    category = 'DOCUMENTS'
    result = 'Updated Text'

class text_combine(_base):
    result = 'Combined Text'

class text_split(_base):
    result = 'Split Text'

class text_changecase(_base):
    result = 'Updated Text'

class text_match(_base):
    result = 'Matches'

class text_match_getgroup(_base):
    result = 'Text'