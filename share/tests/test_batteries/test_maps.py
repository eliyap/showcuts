## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *


class test_maps(TestCase):
    reference_image = ''
    actionID = '95715bf2c0184f57aa6eb54e779e7f9e'

    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(__class__.actionID)

    def tearDown(self):
        del self.actions

    def test_all_actions_loaded(self):
        test_for_errors(self)
        test_no_not_implemented(self)


    # Tailored Tests

    def test_glyphs_correct(self):
        [test_correct_glyph(self, action, 'Maps.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'MAPS') for action in self.actions[0:15]]
        [self.assertEqual(action['category'], 'STREET ADDRESS') for action in self.actions[15:18]]
        [self.assertEqual(action['category'], 'MAPS') for action in self.actions[18:]]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {'class':'', 'value':'Get maps URL from'},
            {'class':'magic empty', 'value':'Location'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':'', 'value':'Get maps URL from'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':'', 'value':'Show'},
            {'class':'magic empty', 'value':'Location'},
            {'class':'', 'value':'in Maps'},
        ])
        compare_elements(self, 'title', 3, [
            {'class':'', 'value':'Show'},
            {'class':'magic', 'value':'Current Location'},
            {'class':'', 'value':'in Maps'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Mode','glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'time from'},
            {'class':'magic', 'value':'Start Location','glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'to'},
            {'class':'magic', 'value':'End Location','glyph':'assets/cat/Ask.svg'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Driving'},
            {'class':'', 'value':'time from'},
            {'class':'magic', 'value':'Current Location'},
            {'class':'', 'value':'to'},
            {'class':'magic empty', 'value':'End Location'},
        ])
        compare_elements(self, 'title', 6, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Walking'},
            {'class':'', 'value':'time from'},
            {'class':'magic', 'value':'Current Location'},
            {'class':'', 'value':'to'},
            {'class':'magic', 'value':'Current Location'},
        ])
        compare_elements(self, 'title', 7, [
            {'class':'', 'value':'Show'},
            {'class':'magic', 'value':'Mode','glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'directions to'},
            {'class':'magic', 'value':'Destination','glyph':'assets/cat/Ask.svg'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':'', 'value':'Show'},
            {'class':'magic', 'value':'Transit'}, # NOTE: actually, this is 'Public Transport', but it might be language preference. Going to leave it, as this error isn't important / unsightly / game-breaking
            {'class':'', 'value':'directions to'},
            {'class':'magic empty', 'value':'Destination'},
        ])
        compare_elements(self, 'title', 9, [
            {'class':'', 'value':'Show'},
            {'class':'magic', 'value':'Transit'},
            {'class':'', 'value':'directions to'},
            {'class':'magic', 'value':'NDCS'},
        ])
        compare_elements(self, 'title', 10, [
            {'class':'', 'value':'Get distance from'},
            {'class':'magic', 'value':'Start Location','glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'to'},
            {'class':'magic', 'value':'End Location','glyph':'assets/cat/Ask.svg'},
        ])
        compare_elements(self, 'lines', 10, [
            {'label':'Route Type', 'class':'magic', 'value':'Ask Each Time','glyph':'assets/cat/Ask.svg'},
            {'label':'Unit', 'class':'magic', 'value':'Ask Each Time','glyph':'assets/cat/Ask.svg'},
        ])
        compare_elements(self, 'title', 11, [
            {'class':'', 'value':'Get distance from'},
            {'class':'magic', 'value':'Current Location'},
            {'class':'', 'value':'to'},
            {'class':'magic empty', 'value':'End Location'},
        ])
        compare_elements(self, 'lines', 11, [
            {'label':'Route Type', 'class':'pill', 'value':[
                {'selected':False,'value':'Direct'},
                {'selected':False,'value':'Driving'},
                {'selected':True ,'value':'Walking'},
            ]},
            {'label':'Unit', 'class':'pill', 'value':[
                {'selected':True,'value':'Miles'},
                {'selected':False ,'value':'Kilometers'}, # NOTE: actually, this is 'Kilometres', but it might be language preference. Going to leave it, as this error isn't important / unsightly / game-breaking
            ]},
        ])
        compare_elements(self, 'title', 12, [
            {'class':'', 'value':'Get distance from'},
            {'class':'magic', 'value':'Current Location'},
            {'class':'', 'value':'to'},
            {'class':'magic empty', 'value':'End Location'},
        ])
        compare_elements(self, 'lines', 12, [
            {'label':'Route Type', 'class':'pill', 'value':[
                {'selected':True ,'value':'Direct'},
                {'selected':False,'value':'Driving'},
                {'selected':False,'value':'Walking'},
            ]},
            {'label':'Unit', 'class':'pill', 'value':[
                {'selected':False,'value':'Miles'},
                {'selected':True ,'value':'Kilometers'}, # NOTE: actually, this is 'Kilometres', but it might be language preference. Going to leave it, as this error isn't important / unsightly / game-breaking
            ]},
        ])
        compare_elements(self, 'title', 13, [
            {'class':'', 'value':'Get addresses from'},
            {'class':'magic empty', 'value':'Input'},
        ])
        compare_elements(self, 'title', 14, [
            {'class':'', 'value':'Get addresses from'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        # @EXPECTED FAILURE: not yet fixed ask text
        # compare_elements(self, 'lines', 15, [
        #     {'label':'Line 1', 'class':'inline specify leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
        #     {'label':'Line 2', 'class':'inline specify leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
        #     {'label':'Town/City', 'class':'inline specify leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
        #     {'label':'County', 'class':'inline specify leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
        #     {'label':'Postcode', 'class':'inline specify leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
        #     {'label':'Region', 'class':'inline specify leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},  
        # ])
        compare_elements(self, 'lines', 16, [
            {'label':'Line 1', 'class':'specify empty leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
            {'label':'Line 2', 'class':'specify empty leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
            {'label':'Town/City', 'class':'specify empty leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
            {'label':'County', 'class':'specify empty leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
            {'label':'Postcode', 'class':'specify empty leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},
            {'label':'Region', 'class':'specify empty leftify', 'value':[{'class': 'magic', 'value': 'Ask Each Time', 'glyph': 'assets/cat/Ask.svg', 'UUID': ''}]},  
        ])
