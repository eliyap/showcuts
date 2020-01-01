## Dependency: 
import logging, re

# Dependency: django boilerplate
from django.template import engines, TemplateSyntaxError

## Dependency: local
from share.process.sc_action import action
from share.process.sc_action.directory import categorize_action
from share.process.lookups._directory import error_action
from showcuts.local_settings import DEBUG

def make_html(WFaction_list: [dict]) -> [dict]:
    indent_level = 0
    action_blocks = []
    UUID_glyphs = {} # maps result UUIDs to their respective glyphs

    for WFaction in WFaction_list:
        action_cat = categorize_action(WFaction['WFWorkflowActionIdentifier'])
        try:
            sc_action = action_cat(WFaction) # instantiate chosen class
            sc_action.to_django(UUID_glyphs, indent_level)
        except:
            sc_action = error_action()
            if DEBUG:raise
        action_blocks.append(sc_action.__dict__)
        indent_level += sc_action.indent_delta # update indentation
        UUID_glyphs[sc_action.UUID] = re.sub('assets/cat/','',sc_action.glyph) # update UUID glyph dict
    return action_blocks, UUID_glyphs
