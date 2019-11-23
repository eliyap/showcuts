
import json
class action:
    def __init__(self, dct:dict):
        self.name = dct['WFWorkflowActionIdentifier']
        try:
            self.UUID = dct['WFWorkflowActionParameters']['UUID']
            dct['WFWorkflowActionParameters'].pop('UUID')
        except:
            self.UUID = 'null'
        self.parameters = dct['WFWorkflowActionParameters']