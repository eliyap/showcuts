import re

from ..base_line import line
from ..title.choose import choose
from ..magic_helpers import AddField

class line_choose(line, choose):
    def __init__(
        self, 
        label:str, 
        key:str,
        ask_each_time:str, 
        default:str,
        options:[str],
        leftify=False,
    ):
        line.__init__(self, label, leftify)
        choose.__init__(self, key, ask_each_time, default, options)

    @AddField('choose')
    def to_html(self, params, UUID_glyphs):
        elem = {
            **line.to_html(self),
            **choose.to_html(self, params, UUID_glyphs)[0], # extract from list
        }
        elem['class'].append('choose')
        # if value isn't in the list of options, 
        # then it is a magic variable (e.g. Ask Each Time)
        if elem['value'] in self.options:
            elem['class'].remove('magic')
        return [elem]