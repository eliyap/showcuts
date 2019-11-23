## Dependency: 
import logging

# Dependency: django boilerplate
from django.template import engines, TemplateSyntaxError

## Dependency: local
from . import action, to_html
from .pieces import error_action

def make_html(action_dct: [dict]) -> [dict]:
    indent_level = 0
    action_blocks = []
    actions = [action.action(i) for i in action_dct]
    UUID_glyphs = {}
    [UUID_glyphs.update({i.UUID:''}) for i in actions]
    for comp in actions:
        try:
            (action_elem, indent) = to_html.format_action(comp, indent_level)
        except:
            (action_elem, indent) = (error_action(), 0)
            #raise #for debugging
        UUID_glyphs[comp.UUID] = action_elem['glyph']
        indent_level += indent # modify indentation for future actions
        action_blocks.append(action_elem)
    return action_blocks, UUID_glyphs
