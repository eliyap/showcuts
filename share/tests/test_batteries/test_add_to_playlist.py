## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '92954432e87444a4b009dfa217c18010'

class test_add_to_playlist(TestCase):
    '''Tests for Add to Playlist action.
    
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
        [test_correct_glyph(self, action, 'Music.png')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'MUSIC') for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Add',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },{
                'class': ['text'], 
                'value': 'to',
            },{
                'class': ['magic'], 
                'value': 'My Music Library',
            },
        ])

        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Add',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },{
                'class': ['text'], 
                'value': 'to',
            },{
                'class': ['magic'], 
                'value': 'My Music Library',
            },
        ])

        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Add',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },{
                'class': ['text'], 
                'value': 'to',
            },{
                'class': ['magic'], 
                'value': 'Playlist',
                'glyph': 'assets/cat/Ask.svg',
            },
        ])

        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Add',
            },{
                'class': ['magic'], 
                'value': 'Updated Playlist',
            },{
                'class': ['text'], 
                'value': 'to',
            },{
                'class': ['magic'], 
                'value': 'Updated Playlist',
            },
        ])

        compare_elements(self, 'title', 4, [
            {
                'class': ['text'], 
                'value': 'Add',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },{
                'class': ['text'], 
                'value': 'to',
            },{
                'class': ['magic'], 
                'value': 'Anime',
            },
        ])