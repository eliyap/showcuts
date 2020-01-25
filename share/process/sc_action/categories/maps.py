from share.process.components._directory import *
from ..action import *

class _base(action):
    category = 'MAPS'
    glyph = 'system/Maps.png'

class getdistance(_base):
    name = 'Get Distance'
    title = [
        text('Get distance from'),
        location(
            'WFGetDirectionsCustomLocation',
            blank_text=None,
            ask_each_time='Start Location',
            default='Current Location',
        ),
        text('to'),
        location(
            'WFGetDistanceDestination',
            blank_text='End Location',
            ask_each_time='End Location',
            default=None,
        )
    ]
    lines = [
        line_pill(
            'Route Type',
            'WFGetDirectionsActionMode',
            ask_each_time='Ask Each Time',
            default='Direct',
            options=['Direct','Driving', 'Walking'],
        ),
        line_pill(
            'Unit',
            'WFDistanceUnit',
            ask_each_time='Ask Each Time',
            default='Kilometers', # NOTE: not kilometres! re vs er
            options=['Miles','Kilometers'],
        ),
    ]
    result = 'Distance'

class gethalfwaypoint(_base):
    name = 'Get Halfway Point'
    title = [
        text('Get halfway point between'),
        location(
            'WFGetHalfwayPointFirstLocation',
            blank_text='First Location',
            ask_each_time='First Location',
            default=None,
        ),
        text('to'),
        location(
            'WFGetHalfwayPointSecondLocation',
            blank_text='Second Location',
            ask_each_time='Second Location',
            default=None,
        ),
    ]
    result = 'Halfway Point'

class gettraveltime(_base):
    name = 'Search Travel Time'
    title = [
        text('Get'),
        choose(
            'WFGetDirectionsActionMode',
            ask_each_time='Mode',
            default='Driving',
            options=[
                'Driving',
                'Walking',
                'Public Transport', # displayed as 'Transit'
            ],
        ),
        text('time from'),
        location(
            'WFGetDirectionsCustomLocation',
            blank_text=None,
            ask_each_time='Start Location',
            default='Current Location',
        ),
        text('to'),
        location(
            'WFDestination',
            blank_text='End Location',
            ask_each_time='End Location',
            default=None,
        ),
    ]
    result = 'Travel Time'

class address(_base):
    name = 'Street Address'
    category = 'STREET ADDRESS'
    lines = [
        line_inline(
            'Line 1',
            'WFAddressLine1',
            blank_text='44 Planter Road',
            leftify=True,
        ), # defaults to the device owner country (ignored)
        line_inline(
            'Line 2',
            'WFAddressLine2',
            blank_text='Text',
            leftify=True,
        ),
        line_inline(
            'Town/City',
            'WFCity',
            blank_text='Swindon',
            leftify=True,
        ),
        line_inline(
            'County',
            'WFState',
            blank_text='Wiltshire',
            leftify=True,
        ),
        line_inline(
            'Postcode',
            'WFPostalCode',
            blank_text='SN2 7BP',
            leftify=True,
        ),
        line_inline(
            'Region',
            'WFCountry',
            blank_text='United Kingdom',
            leftify=True,
        ),
    ]
    result = 'Street Address'

class getmapslink(_base):
    name = 'Get Maps URL'
    title = [
        text('Get maps URL from'),
        magic(
            'WFInput',
            blank_text='Location',
            ask_each_time=None,
        )
    ]
    result = 'Maps URL'

class getdirections(_base):
    name = 'Show Directions'
    title = [
        text('Show'),
        choose(
            'WFGetDirectionsActionMode',
            ask_each_time='Mode',
            default='Driving',
            options=[
                'Driving',
                'Walking',
                'Public Transport', # displayed as 'Transit'
            ],
        ),
        text('directions to'),
        location(
            'WFDestination',
            blank_text='Destination',
            ask_each_time='Destination',
            default=None,
        ),
    ]

class searchmaps(_base):
    name = 'Show in Maps'
    title = [
        text('Show'),
        location(
            'WFInput',
            blank_text='Location',
            ask_each_time='Location',
            default=None,
        ),
        text('in Maps'),
    ]

class searchlocalbusinesses(_base):
    name = 'Search Local Businesses'
    result = 'Local Businesses'