def control_flow(parameters: dict) -> (str, str, int):
    UUID = parameters.get('UUID', None)
    group = parameters.get('GroupingIdentifier')
    mode = parameters.get('WFControlFlowMode')
    return (UUID, group, mode)
