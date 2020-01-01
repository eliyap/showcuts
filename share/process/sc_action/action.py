class action:
    category = 'MISSING'
    glyph    = 'Missing.svg'

    result   = None # default name for Magic Variable Result
    UUID     = 'null' # UUID identifying the action's output
    
    title    = [] # Shortcut Title (larger text at the top)
    lines    = [] # Lines, usually containing extra actions
    items    = [] # Special field for Dictionary Items
    
    indent       = 0 # indentation level of action
    indent_delta = 0 #  change in future indentation level
    css_class = [] # special CSS classes for special actions

    def __init__(self, dct:dict):
        try:
            self.UUID = dct['WFWorkflowActionParameters']['UUID']
            dct['WFWorkflowActionParameters'].pop('UUID')
        except:
            self.UUID = 'null'

        self.parameters = dct['WFWorkflowActionParameters']
    
    def inherit(self):
        self.category = self.__class__.category
        self.glyph = f'assets/cat/{self.__class__.glyph}'
        self.result = self.__class__.result

        self.title = self.__class__.title
        self.lines = self.__class__.lines
        self.items = self.__class__.items
        
    def to_django(
        self, 
        UUID_glyphs:dict,
        indent:int,
    ):
        self.indent = indent
        # copy (inherited) glyph, category, & result from class to instance
        self.inherit()
        
        title_ = []
        for element in self.title:
            title_.extend(element.to_html(self.parameters, UUID_glyphs))
        self.title = title_
        
        lines_ = []
        for element in self.lines:
            lines_.extend(element.to_html(self.parameters, UUID_glyphs))
        self.lines = lines_
        
        items_ = []
        for element in self.items:
            items_.extend(element.to_html(self.parameters, UUID_glyphs))
        self.items = items_

        # post processing, including logic between elements
        self.modify()

    def modify(self):
        pass # should be overriden

    ## Function: hide a specific line
    def hide_line(self, label:str):
        for line in self.lines:
            if line['label'] == label:
                if 'hidden' not in line['class']: # prevent duplicates
                    line['class'].append('hidden')
                return
        raise ValueError(f'No line with label "{label}"')
    
    ## Function: return a labelled line obj
    def get_line(self, label:str):
        for line in self.lines:
            if line['label'] == label:
                return line
        raise ValueError(f'No line with label "{label}"')
        

    @classmethod
    def action_hook(cls, dct:dict):
        if 'indent' in dct and 'UUID' in dct:
            sc_action = cls({'WFWorkflowActionParameters':{}})
            for key in [
                'category',
                'glyph',
                'result',
                'title',
                'lines',
                'items',
                'css_class',
                'indent',
                'UUID',
            ]:
                if key in dct:
                    setattr(sc_action, key, dct[key])
            return sc_action
        else:
            return dct

class control:
    def flow_mode(self):
        return self.parameters['WFControlFlowMode']
    
    def get_delta(self):
        return {
            0: +1, # head block, indents everything inside
            1: 0, # used for menu items
            2: -1, # returns indentation to previous
        }[self.flow_mode()]

    def mod_indent(self):
        self.indent += {
            0: 0,
            1: -1,
            2: -1,
        }[self.flow_mode()]
        self.css_class.append(
            {
                0: '',
                1: ' control',
                2: ' control',
            }[self.flow_mode()]
        )
        self.indent_delta = self.get_delta()