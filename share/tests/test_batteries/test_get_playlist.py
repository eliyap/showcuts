## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = 'aea1999225dc49a38038521ccf350089'

class test_get_playlist(TestCase):
    '''Tests for Get Playlist action.

    Written 20.01.13
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
        [test_correct_glyph(self, action, 'Music.png')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'MUSIC') for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Get songs in',
            },{
                'class': ['magic','empty'], 
                'value': 'Playlist',
            },
        ])
        
        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Get songs in',
            },{
                'class': ['magic','empty'], 
                'value': 'Playlist',
            },
        ])
        
        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Get songs in',
            },{
                'class': ['magic'], 
                'value': 'Playlist',
                'glyph': 'assets/cat/Ask.svg',
            },
        ])
        
        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Get songs in',
            },{
                'class': ['magic'], 
                'value': 'Playlist',
            },
        ])
        
        compare_elements(self, 'title', 4, [
            {
                'class': ['text'], 
                'value': 'Get songs in',
            },{
                'class': ['magic'], 
                'value': 'Anime',
            },
        ])
        