from ..action import *

class _base(action):
    category = 'MAPS'
    glyph = 'system/Maps.png'

class getdistance(_base):
    result = 'Distance'

class gethalfwaypoint(_base):
    result = 'Halfway Point'

class gettraveltime(_base):
    result = 'Travel Time'

class address(_base):
    category = 'STREET ADDRESS'
    result = 'Street Address'

class getmapslink(_base):
    result = 'Maps URL'

class getdirections(_base):
    pass

class searchmaps(_base):
    pass

class searchlocalbusinesses(_base):
    result = 'Local Businesses'