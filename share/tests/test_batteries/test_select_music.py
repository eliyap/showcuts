## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '06c7737fab6e48ac8f2859366c9883d2'

class test_select_music(TestCase):
    '''Tests for Select Music action.
    
    Written 20.01.11
    '''
    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(actionID)
        # remove comment actions
        self.actions.pop(8) # set var action
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
        [test_correct_glyph(self, action, 'Music.png')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'MUSIC')
         for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Select music',
            },
        ]) # no variation in the title
        compare_elements(self, 'lines', 0, [
            {
                'label':'Select Multiple Songs',
                'class': ['toggle','off'], 
                'value': '',
            },
        ])
       
        compare_elements(self, 'lines', 1, [
            {
                'label':'Select Multiple Songs',
                'class': ['toggle','off'], 
                'value': '',
            },
        ])
        
        compare_elements(self, 'lines', 2, [
            {
                'label':'Select Multiple Songs',
                'class': ['magic'], 
                'value': 'Ask Each Time',
            },
        ])
        
        compare_elements(self, 'lines', 3, [
            {
                'label':'Select Multiple Songs',
                'class': ['toggle','on'], 
                'value': '',
            },
        ])

        compare_elements(self, 'lines', 4, [
            {
                'label':'Select Multiple Songs',
                'class': ['magic'], 
                'value': 'X',
            },
        ])