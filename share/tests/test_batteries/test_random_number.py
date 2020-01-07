## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '406710b35d834b5d94abc74250b9df9b'

class test_random_number(TestCase):
    '''Tests for Calculate Statistics action.
    
    Written 20.01.05
    '''
    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(actionID)
        # remove comment actions
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
        [test_correct_glyph(self, action, 'Math.svg')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'MATHS')
         for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Random number between'
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Minimum',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'and'
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Maximum',
                'field':'number',
            },
        ])
        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Random number between'
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Minimum',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'and'
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Maximum',
                'field':'number',
            },
        ])
        
        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Random number between'
            },
            {
                'class': ['magic',], 
                'value': '-.5',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'and'
            },
            {
                'class': ['magic'], 
                'value': '20000000000000000000000000000000',
                'field':'number',
            },
        ])
        
        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Random number between'
            },
            {
                'class': ['magic'], 
                'value': 'Minimum',
                'glyph': 'assets/cat/Ask.svg',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'and'
            },
            {
                'class': ['magic'], 
                'value': 'Maximum',
                'glyph': 'assets/cat/Ask.svg',
                'field':'number',
            },
        ])
        