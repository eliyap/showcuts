## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '22795e014347497fb01f7bab5d1a0444'

class test_create_playlist(TestCase):
    '''Tests for Create Playlist action.
    NOT FINISHED! inline elements are giving me trouble
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
                'value': 'Create playlist',
            },{
                'class': ['magic','empty'], 
                'value': 'Playlist Name',
            },{
                'class': ['text'], 
                'value': 'with',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },
        ])
        compare_elements(self, 'lines', 0, [
            {
                'label': 'Author',
                'class': ['inline-line','empty'], 
                'value': [
                    {
                        'class': [],
                        'attrs': {},
                        'value': 'Shortcuts',
                    },
                ],
            },{
                'label': 'Description',
                'class': ['inline-line','empty'], 
                'value': [
                    {
                        'class': [],
                        'attrs': {},
                        'value': 'All my favorites',
                    },
                ],
            },
        ])

        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Create playlist',
            },{
                'class': ['magic','empty'], 
                'value': 'Playlist Name',
            },{
                'class': ['text'], 
                'value': 'with',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },
        ])
        compare_elements(self, 'lines', 1, [
            {
                'label': 'Author',
                'class': ['inline-line','empty'], 
                'value': [
                    {
                        'class': [],
                        'attrs': {},
                        'value': 'Shortcuts',
                    },
                ],
            },{
                'label': 'Description',
                'class': ['inline-line','empty'], 
                'value': [
                    {
                        'class': [],
                        'attrs': {},
                        'value': 'All my favorites',
                    },
                ],
            },
        ])

        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Create playlist',
            },{
                'class': ['inline-magic'], 
                'value': [
                    {
                        'class': ['magic'],
                        'value': 'Text',
                        'attrs': {},
                    },
                ],
            },{
                'class': ['text'], 
                'value': 'with',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },
        ])
        compare_elements(self, 'lines', 2, [
            {
                'label': 'Author',
                'class': ['inline-line','empty'], 
                'value': [
                    {
                        'class': ['magic'],
                        'value': 'Text',
                        'attrs': {},
                    },
                ],
            },{
                'label': 'Description',
                'class': ['inline-line','empty'], 
                'value': [
                    {
                        'class': ['magic'],
                        'value': 'Text',
                        'attrs': {},
                    },
                ],
            },
        ])

