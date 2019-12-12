from .components import make_magic, magic

def conditional(parameters:dict) -> list:
    condition = parameters.get('WFCondition', None)
    # condensed check for 'Current Date' / 'Clipboard' Magic Var
    try:
        var_type = parameters['WFInput']['Type']
    except KeyError:
        var_type = None
    return cond_mapper(parameters, condition, var_type)

condition_map = { # (*) => there's an alternate form of this condition
    0:'is less than', # *
    1:'is less than or equal to',
    2:'is greater than', # *
    3:'is greater than or equal to',
    4:'is', # *
    5:'is not', # *
    8:'begins with',
    9:'ends with',
    99:'contains',
    999:'does not contain',
    100:'has any value',
    101:'does not have any value',
    1000:'is in the next',
    1001:'is in the last',
    1002:'is today',
    1003:'is between',
}

def cond_mapper(parameters, condition, var_type):
    if None == condition:
        return [magic('Condition', True)]
    
    elif condition in [0, 2]:
        if 'CurrentDate' == var_type:
            condition_elem = magic('is after' if condition == 0 else 'is before')
            test_elem = make_magic(parameters, 'WFDate', 'Date')
        elif 'WFNumberValue' in parameters:  # can't detect number?
            condition_elem = magic('is less than' if condition == 0 else 'is greater than')
            test_elem = make_magic(parameters, 'WFNumberValue', 'Number')
        else:  # catch all
            condition_elem = magic('is less than' if condition == 0 else 'is greater than')
            test_val = parameters.get('WFDate', parameters.get('WFConditionalActionString', parameters.get('Number', None)))
            test_elem = magic(test_val) if test_val else magic('Value', True)
        return [
            condition_elem,
            test_elem,
        ]
    
    elif condition in [1, 3]:
        return [
            magic(condition_map[condition]),
            make_magic(parameters, 'WFNumberValue', 'Number'),
        ]
    
    elif condition in [4, 5]:
        if 'CurrentDate' == var_type:
            condition_elem = magic('is exactly' if condition == 4 else 'is not exactly')
            test_elem = make_magic(parameters, 'WFDate', 'Date')
        elif 'Clipboard' == var_type:
            condition_elem = magic('is' if condition == 4 else 'is not')
            test_elem = make_magic(parameters, 'WFConditionalActionString', 'Text')
        # can't detect number?
        elif 'WFNumberValue' in parameters:
            condition_elem = magic('is' if condition == 4 else 'is not')
            test_elem = make_magic(parameters, 'WFNumberValue', 'Number')
        else:  # catch all
            condition_elem = magic('is' if condition == 4 else 'is not')
            test_val = parameters.get('WFDate', parameters.get('WFConditionalActionString', parameters.get('Number', None)))
            test_elem = magic(test_val) if test_val else magic('Value', True)
        return [
            condition_elem,
            test_elem,
        ]
    
    elif condition in [8, 9]:
        return [
            magic(condition_map[condition]),
            make_magic(parameters, 'WFConditionalActionString', 'Text'),
        ]
    
    elif condition in [99, 999]:
        return [
            magic(condition_map[condition]),
            make_magic(parameters, 'WFConditionalActionString', 'Text'),
        ]
    
    elif condition in [100, 101]:
        return [condition_map[condition]]
    
    elif condition in [1000, 1001]:
        return [
            magic(condition_map[condition]),
            make_magic(parameters, 'WFDuration', 'Number', False, 'Magnitude'),
            # no blank, 'minutes' is chosen by default
            make_magic(parameters, 'WFDuration','unit', False, 'Unit')
        ]
    
    elif 1002 == condition:
        return [magic(condition_map[condition])]
    
    elif 1003 == condition:
        if 'WFDate' in parameters and 'WFAnotherDate' in parameters:
            test_elem_1 = make_magic(parameters, 'WFDate', 'Date')
            test_elem_2 = make_magic(parameters, 'WFAnotherDate', 'Date')
        elif 'WFNumberValue' in parameters and 'WFAnotherNumber' in parameters:
            test_elem_1 = make_magic(parameters, 'WFNumberValue', 'Date')
            test_elem_2 = make_magic(parameters, 'WFAnotherNumber', 'Date')
        else:  # catch all
            test_elem_1 = magic('Value', True)
            test_elem_2 = magic('Value', True)
        return [
            magic(condition_map[condition]),
            test_elem_1,
            'and',
            test_elem_2,
        ]
    
    else:
        return [magic('Condition', True)]