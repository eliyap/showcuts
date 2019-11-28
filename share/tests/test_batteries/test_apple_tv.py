## Dependency: sys
from unittest import TestCase
import logging


# Dependency: battery testing
from share.tests.test_batteries.battery import *

reference_image = 'https://i.imgur.com/ztBeFnj.png'
actionID = '09596dcc51644fe58625fcb1d13d57e5'


class test_apple_tv(TestCase):

    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(actionID)

    def tearDown(self):
        del self.actions

    def test_all_actions_loaded(self):
        test_for_errors(self)
        test_no_not_implemented(self)

    # Tailored Tests

    def test_glyphs_correct(self):
        [test_correct_glyph(self, action, 'Remote.png')
         for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'APPLE TV REMOTE')
         for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class': '', 'value': 'Open App on'},
            {'class': 'magic empty', 'value': 'Apple TV'},
        ])
        compare_titles(self, 1, [
            {'class': '', 'value': 'Open'},
            {'class': 'magic', 'value': 'TV'},
            {'class': '', 'value': 'on'},
            {'class': 'magic', 'value': 'Apple TV'},
        ])
        compare_titles(self, 2, [
            {'class': '', 'value': 'Show remote control for'},
            {'class': 'magic empty', 'value': 'Apple TV'},
        ])
        compare_titles(self, 3, [
            {'class': '', 'value': 'Show remote control for'},
            {'class': 'magic', 'value': 'Apple TV'},
        ])
        compare_titles(self, 4, [
            {'class': 'magic', 'value': 'Pause'},
            {'class': 'magic empty', 'value': 'Apple TV'},
        ])
        compare_titles(self, 5, [
            {'class': 'magic', 'value': 'Media Command'},
            {'class': 'magic', 'value': 'Apple TV'},
        ])
        compare_titles(self, 6, [
            {'class': '', 'value': 'Sleep'},
            {'class': 'magic empty', 'value': 'Apple TV'},
        ])
        compare_titles(self, 7, [
            {'class': '', 'value': 'Sleep'},
            {'class': 'magic', 'value': 'Apple TV'},
        ])
        compare_titles(self, 8, [
            {'class': '', 'value': 'Wake'},
            {'class': 'magic empty', 'value': 'Apple TV'},
        ])
        compare_titles(self, 9, [
            {'class': '', 'value': 'Wake'},
            {'class': 'magic', 'value': 'Apple TV'},
        ])
