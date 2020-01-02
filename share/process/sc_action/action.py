class action:
    """
    Represents a single \"action\" in a shortcut.
    """

    #: The action's category (e.g. SCRIPTING or MATH). Always in ALL CAPS.
    #: 
    #: May be excluded for control-flow blocks, such as the If block's `End If`.
    category = '' 

    #: The action's glyph, usually matching the category. 
    #: If there is no category, there is also no glyph, and vice versa.
    #: 
    #: Actions donated from an app have the app icon as their glyph
    glyph    = '' 

    #: Every action may (or may not) produce one `result`, 
    #: which may (or may not) be given a custom name.
    #: 
    #: This field define's the action's default result name (if any). ``None`` means the action does not produce a result.
    result   = None 

    #: UUID string identifying the ``result`` variable produced by the action.
    #: 
    #: Used to link result variables to their origin.
    UUID     = 'null'
    
    #: List of element objects composing the title (large head text).
    #: 
    #: Populated with ``text`` objects, and children of ``base_magic``.
    title    = []

    #: List of additional options customizing an action's behaviour.
    #: 
    #: Populated with ``line_${elem}`` objects.
    lines    = []

    #: List of keys and values particular to the Dictionary action.
    items    = []
    
    #: Visual indentation level for actions inside control flow blocks.
    #: 
    #: Control flow blocks may be nested indefinitely, 
    #: but stop visually indenting after 8 levels.
    indent       = 0
    
    #: Determines whether subsequent actions are (un)-indented. Permitted values: -1, 0, +1.
    #: 
    #: :todo: Check whether indentation delta is either -1, 0, or +1.
    indent_delta = 0 #  change in future indentation level

    #: List of CSS classes (str) to apply to special actions (e.g. Comment action)
    css_class = []

    def __init__(self, dct:dict):

        try:
            self.UUID = dct['WFWorkflowActionParameters']['UUID']
            dct['WFWorkflowActionParameters'].pop('UUID')
        except:
            self.UUID = 'null'

        self.parameters = dct['WFWorkflowActionParameters']
    
    def inherit(self):
        '''
        Copies (inherited) class variables to instance.

        Allows us to make defining actions with similar 
        ``category``, ``glyph``, and ``result`` DRYer.

        Creates instance specific `title`, `lines`, and `elem`
        so that their values may be individually set.
        '''

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
        '''
        Invokes ``to_html`` method of every object in ``title``, ``lines``, and ``elem``,
        transforming these into lists of ``dict`` for the Django template engine.

        Invokes action's ``modify`` method last.
        '''
        self.indent = indent
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
        '''
        Called after ``to_html`` has been invoked on ``title``, ``lines``, and ``elem``.

        Houses special logic for each action. 
        Usually, this means hiding element `X` if element `Y` has value `Z`.

        Meant to be overriden.
        '''

        pass

    def hide_line(self, label:str):
        '''
        Add the "hidden" CSS class to particular element in ``lines``, 
        as identified by its ``label``.

        Raises ValueError if the label does not a match a line.
        '''

        for line in self.lines:
            if line['label'] == label:
                if 'hidden' not in line['class']: # prevent duplicates
                    line['class'].append('hidden')
                return
        raise ValueError(f'No line with label "{label}"')
    
    def get_line(self, label:str):
        '''
        Return a particular element in ``lines``, as identified by its ``label``. 
        Usually used in ``modify`` to pick a line out for modification

        Raises ValueError if the label does not a match a line.
        '''

        for line in self.lines:
            if line['label'] == label:
                return line
        raise ValueError(f'No line with label "{label}"')
        
    @classmethod
    def action_hook(cls, dct:dict):
        '''
        Used to deserialize ``action`` objects from JSON.
        '''

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
    '''
    Represents a control flow action such as `If`, `Repeat`, or `Choose from Menu`.
    '''

    def flow_mode(self):
        '''
        Looks up the action's `WFControlFlowMode`.
        '''

        return self.parameters['WFControlFlowMode']
    
    def mod_indent(self):
        '''
        Adjusts action based on it's ``flow_mode`` value

        :0: Head block
        * Has a category & glyph
        * Accepts parameters
        * Indents inner actions by +1

        :1: Body block
        * No category or glyph
        * Does not accept parameters
        * Unindented 1 level from inner blocks (same indentation as Head)
        * Does not change indentation of subsequent blocks

        :2: Foot block
        * No category or glyph
        * Does not accept parameters
        * Unindented 1 level from inner blocks (same indentation as Head)
        * Unindents subsequent blocks -1.
        '''

        # adjust own indent
        self.indent += {
            0: 0,
            1: -1,
            2: -1,
        }[self.flow_mode()]

        # add `control` class to remove category and glyph
        self.css_class += {
            0: [],
            1: ['control'],
            2: ['control'],
        }[self.flow_mode()]

        # Returns the correct `indent_delta` value based on the `flow_mode`
        self.indent_delta = {
            0: +1, # head block, indents everything inside
            1: 0, # used for menu items
            2: -1, # returns indentation to previous
        }[self.flow_mode()]