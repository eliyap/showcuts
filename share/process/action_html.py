## Dependency: 
import logging

# Dependency: django boilerplate
from django.template import engines, TemplateSyntaxError

## Dependency: local
from share.process.action import action
from share.process.to_html import format_action
from share.process.pieces import error_action
from showcuts.local_settings import DEBUG

def make_html(action_dct: [dict]) -> [dict]:
    indent_level = 0
    action_blocks = []
    actions = [action(i) for i in action_dct]
    UUID_glyphs = {}
    [UUID_glyphs.update({i.UUID:''}) for i in actions]
    for comp in actions:
        try:
            (action_elem, indent) = format_action(comp, indent_level)
        except:
            (action_elem, indent) = (error_action(), 0)
            if DEBUG:raise
        UUID_glyphs[comp.UUID] = action_elem['glyph']
        indent_level += indent # modify indentation for future actions
        action_blocks.append(action_elem)
    return action_blocks, UUID_glyphs
