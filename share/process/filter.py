## Dependency: sys
import logging

from .conditional import *
from .components import get_inline
from .pieces import field_type

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
            ] + 
            filter_mapper(
                fltr['Values'], 
                fltr['Operator'], 
                field_type[fltr['Property']]
            ),
            'class': 'inline', 
        }}]
    return filter_lines

def filter_mapper(parameters, condition, var_type):
    if None == condition:
        return [magic('Condition', True)]
    
    elif condition in [0, 2]:
        if 'date' == var_type:
            return date_1(parameters)
        elif 'size' == var_type:
            return size_1(parameters)
        elif 'number' == var_type:
            return number(parameters)
        else:  # catch all
            test_val = parameters.get('Date', parameters.get('WFConditionalActionString', parameters.get('Number', None)))
            test_elem = magic(test_val) if test_val else magic('Value', True)
        return [
            test_elem,
        ]
    
    elif condition in [1, 3]:
        if 'date' == var_type:
            return date_1(parameters)
        elif 'size' == var_type:
            return size_1(parameters)
        return [
            make_magic(parameters, 'WFNumberValue', 'Number'),
        ]
    
    elif condition in [4, 5]:
        if 'date' == var_type:
            return date_1(parameters)
        elif 'size' == var_type:
            return size_1(parameters)
        elif 'string' == var_type:
            return text(parameters)
        elif 'duration' == var_type:
            return duration(parameters)
        elif 'bool' == var_type:
            return truefalse(parameters)
        elif 'number' == var_type:
            return number(parameters)
        else:  # catch all
            test_val = parameters.get('Date', parameters.get('WFConditionalActionString', parameters.get('Number', None)))
            test_elem = magic(test_val) if test_val else magic('Value', True)
        return []

    elif condition in [8, 9]:
        return text(parameters)

    
    elif condition in [99, 999]:
        return text(parameters)
        
    
    elif condition in [100, 101]:
        return []
    
    elif condition in [1000, 1001]:
        return duration(parameters)
    
    elif 1002 == condition:
        return []
    
    elif 1003 == condition:
        if 'date' == var_type:
            return date_2(parameters)
        return [ # failsafe
            magic('Value', True),
            'and',
            magic('Value', True),
        ]
    
    else:
        return [magic('Condition', True)]

def size_1(parameters):
    size = {**make_magic(parameters, 'Number', 'anything'),**{'class':'filter-benchmark'}}
    unit = {**make_magic(parameters, 'ByteCountUnit', 1),**{'class':'filter-unit'}}
    unit['value'] = {
        1:'bytes',
        2:'KB',
        4:'MB',
        8:'GB',
        16:'TB',
        32:'PB',
        64:'EB',
        128:'ZB',
    }.get(unit['value'], unit['value'])
    if size['value'] == '1': unit['value'] = unit['value'][:-1]
    return [size,unit]

def date_1(parameters):
    return [{**make_magic(parameters, 'Date', 'Now'),**{'class':'filter-benchmark'}}]

def date_2(parameters):
    return [
        {**make_magic(parameters, 'Date', 'Now'),**{'class':'filter-benchmark'}},
        {'value':'and'},
        {**make_magic(parameters, 'AnotherDate', 'Now'),**{'class':'filter-benchmark'}},
    ]

def duration(parameters):
    size = {**make_magic(parameters, 'Number', 'anything'),**{'class':'filter-benchmark'}}
    unit = {**make_magic(parameters, 'Unit', 4),**{'class':'filter-unit'}}
    unit['value'] = {
        4:'years',
        8:'months',
        8192:'weeks',
        16:'days',
        32:'hours',
        64:'minutes',
    }.get(unit['value'], unit['value'])
    if size['value'] == '1': unit['value'] = unit['value'][:-1]
    return [size,unit]

def text(parameters):
    val = parameters.get('String','anything')
    if isinstance(val, dict):
        return [{**make_magic(parameters, 'String', 'anything'),**{'class':'filter-benchmark inline'}}]
    else: 
        return [{'class':'filter-benchmark','value':val}]

def number(parameters):
    val = parameters.get('Number','anything')
    if isinstance(val, dict):
        return [{**make_magic(parameters, 'Number', 'anything'),**{'class':'filter-benchmark'}}]
    else: 
        return [{'class':'filter-benchmark','value':val}]

def truefalse(parameters):
    val = str(parameters.get('Bool'))
    return [{'class':'filter-benchmark','value':val}]