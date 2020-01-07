from ..action import *

class _base(action):
    category = 'MAPS'
    glyph = 'system/Maps.png'

class getdistance(_base):
    name = 'Get Distance'
    result = 'Distance'

class gethalfwaypoint(_base):
    name = 'Get Halfway Point'
    result = 'Halfway Point'

class gettraveltime(_base):
    name = 'Search Travel Time'
    result = 'Travel Time'

class address(_base):
    name = 'Street Address'
    category = 'STREET ADDRESS'
    result = 'Street Address'

class getmapslink(_base):
    name = 'Get Maps URL'
    result = 'Maps URL'

class getdirections(_base):
    name = 'Show Directions'

class searchmaps(_base):
    name = 'Show in Maps'

class searchlocalbusinesses(_base):
    name = 'Search Local Businesses'
    result = 'Local Businesses'