## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = 'e43107433b084e79aba13187b0a44de1'

class test_calculate_statistics(TestCase):
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
            {'class': ['text'], 'value': 'Calculate the'},
            {'class': ['magic'], 'value': 'Average'},
            {'class': ['text'], 'value': 'of'},
            {'class': ['magic', 'empty'], 'value': 'Input'},
        ])