from .conditional import *

def make_filter(
        metric:str, # e.g. "File Size", in Purple
        condition:str, # e.g. "Is Less Than", in Pink
        standard:str, # e.g. "40MB", in Red
    ):
    return {
    }
def filtration(filter_dct:dict):
    filter_lines = []
    filters = filter_dct['WFActionParameterFilterTemplates']
    if len(filters) > 1:
        filter_lines += [{**{'label':''},**{
            'value': 'All the following are true' if filter_dct['WFActionParameterFilterPrefix'] == 1 else 'Any of the following are true', 
            'class': 'choose-var', 
        }}]
    for fltr in filters:

        filter_lines += [{**{'label':''},**{
            'value': [
                {'class':'filter-property','value':fltr['Property']},
                {'class':'filter-operator','value':condition_map.get(fltr['Operator'],'Condition')},
                {'class':'filter-benchmark','value':'very long test string'},
                {'class':'filter-unit','value':'Lorem Ipsum Dolor Sit Amet'},
            ],
            'class': 'inline', 
        }}]
    return filter_lines