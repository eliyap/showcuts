## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = 'e7e2790c57434d7eb15ceadfba0172eb'

class test_play_pause(TestCase):
    '''Tests for Play/Pause action.
    
    Written 20.01.12
    '''
    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(actionID)
        # remove comment actions
        self.actions.pop(7)
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
        [test_correct_glyph(self, action, 'Play-Pause.svg')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'NOW PLAYING') for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['magic'], 
                'value': 'Play/Pause',
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
                'class': ['magic'], 
                'value': 'Play/Pause',
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
                'class': ['magic'], 
                'value': 'Play/Pause',
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
                'class': ['magic'], 
                'value': 'Ask Each Time',
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
                'class': ['magic'], 
                'value': 'Play/Pause',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        compare_elements(self, 'title', 5, [
            {
                'class': ['magic'], 
                'value': 'Play',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        compare_elements(self, 'title', 6, [
            {
                'class': ['magic'], 
                'value': 'Pause',
            },{
                'class': ['text'], 
                'value': 'on',
            },{
                'class': ['magic'], 
                'value': 'iPhone',
            },
        ])
        