import re

from ..base_line import line
from ..base_magic import base_magic

class line_pill(line, base_magic):
    def __init__(
        self, 
        label:str, 
        key:str,
        ask_each_time:str, 
        default:str,
        options:[str],
    ):
        line.__init__(self, label, leftify=False)
        base_magic.__init__(self, key, ask_each_time)
        self.default = default
        self.options = options

    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, self.default)
        if isinstance(parameter, dict):
            elem = base_magic.to_html(self, params, UUID_glyphs)[0]
        elif isinstance(parameter, str):
            # Find which was chosen, search must be case-insensitive
            elem = {
                'class': ['pill'], 
                'value': [{
                    'class':'pill-on' if option.lower()==parameter.lower() else 'pill-off',
                    'value':option,
                } for option in self.options], 
                'key':self.key,
            }
        return [{
            **line.to_html(self),
            **elem,
        }]