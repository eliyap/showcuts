## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '4173f68c3797491c99e1a5d35ad0c273'

class test_skip_back(TestCase):
    '''Tests for Skip Back action.
    
    Written 20.01.12
    '''
    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(actionID)
        # remove comment actions
        self.actions.pop(6)
        self.actions.pop(4)
        self.actions.pop(2)
        self.actions.pop(0)

    def tearDown(self):
        del self.actions

    def test_all_actions_loaded(self):
        test_for_errors(self)
        test_no_not_implemented(self)

    # Tailored Tests

    def test_glyphs_correct(self):
        [test_correct_glyph(self, action, '.svg')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'NOW PLAYING') for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Skip back to the',
            },{
                'class': ['magic'], 
                'value': 'Beginning',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Skip back to the',
            },{
                'class': ['magic'], 
                'value': 'Beginning',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Skip back to the',
            },{
                'class': ['magic'], 
                'value': 'Skip To',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'Device',
            },
        ])
        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Skip back to the',
            },{
                'class': ['magic'], 
                'value': 'Beginning',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        compare_elements(self, 'title', 4, [
            {
                'class': ['text'], 
                'value': 'Skip back to the',
            },{
                'class': ['magic'], 
                'value': 'Previous Song',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        