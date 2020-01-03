class line:
    '''Base class for line variables.'''

    def __init__(
        self,
        label:str,
        leftify:bool = False, # determines whether the element is left / right aligned
    ):
        '''
        :param label: Label to the left of the parameter, detailing what it is.
        
        :param leftify: Whether or not to flush the variable left against the label. Usually used for ``line_inline``.
        '''
        self.label = label
        self.leftify = leftify

    def to_html(self) -> dict:
        '''Simply returns the label wrapped in a dict.'''
        return {'label':self.label}