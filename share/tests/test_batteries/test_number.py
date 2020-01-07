## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '8ec1111d76ea499daeb11a51f5905bed'

class test_number(TestCase):
    '''Tests for Number action.
    
    Written 20.01.06
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
        [self.assertEqual(action['category'], 'NUMBER')
         for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['magic', 'empty'], 
                'value': '42',
                'field':'number',
            },
        ])
        compare_elements(self, 'title', 1, [
            {
                'class': ['magic', 'empty'], 
                'value': '42',
                'field':'number',
            },
        ])
        compare_elements(self, 'title', 2, [
            {
                'class': ['magic'], 
                'value': '-.5',
                'field':'number',
            },
        ])
        compare_elements(self, 'title', 3, [
            {
                'class': ['magic'], 
                'value': 'Number',
                'glyph': 'assets/cat/Ask.svg',
                'field':'number',
            },
        ])
        