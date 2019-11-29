## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *


class test_specify_date(TestCase):
    reference_image = ''
    actionID = '3fec82e3816e49f6a95236a3e85fdc1c'

    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(__class__.actionID)

    def tearDown(self):
        del self.actions

    def test_all_actions_loaded(self):
        test_for_errors(self)
        #test_no_not_implemented(self)
        # temporarily exempt, as Ask Each Time produces no title elem

    # Tailored Tests

    def test_glyphs_correct(self):
        [test_correct_glyph(self, action, 'Date.svg') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'DATE') for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'magic', 'value':'Current Date'},
        ])
        compare_titles(self, 1, [
            {'class':'magic', 'value':'Specified Date'},
            {'class':'magic', 'value':'29th June 1700'},
        ])
        compare_titles(self, 2, [
            {'class':'magic', 'value':'Specified Date'},
            {'class':'magic empty', 'value':'29 June 2007'},
        ])
        compare_titles(self, 3, [
            # no title elems
            #TODO: test line elems
        ])