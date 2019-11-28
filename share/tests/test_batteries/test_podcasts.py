## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *


class test_simple_settings(TestCase):
    reference_image = 'https://i.imgur.com/guz1FJY.png'
    actionID = '406f03b6ab584adf99fc67f4c6021bbf'

    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(__class__.actionID)

    def tearDown(self):
        del self.actions

    def test_all_actions_loaded(self):
        test_for_errors(self)
        test_no_not_implemented(self)


    # Tailored Tests

    def test_glyphs_correct(self):
        [test_correct_glyph(self, action, 'Podcasts.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'PODCASTS') for action in self.actions]

    def test_titles_correct(self):
        # Play Podcast
        compare_titles(self, 0, [
            {'class':'', 'value':'Play'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_titles(self, 1, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Cortex'},
        ])
        compare_titles(self, 2, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Podcast','glyph':'assets/cat/Ask.svg'},
        ])
        # Get Detail from Podcast
        compare_titles(self, 3, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Podcast episode'},
        ])
        compare_titles(self, 4, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Name'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 5, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        # Get episodes of Podcast
        compare_titles(self, 6, [
            {'class':'', 'value':'Get episodes of'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_titles(self, 7, [
            {'class':'', 'value':'Get episodes of'},
            {'class':'magic', 'value':'Cortex'},
        ])
        compare_titles(self, 8, [
            {'class':'', 'value':'Get episodes of'},
            {'class':'magic', 'value':'Podcast','glyph':'assets/cat/Ask.svg'},
        ])
        # mono
        compare_titles(self, 9, [
            {'class':'', 'value':'Get Podcasts from Library'},
        ])
        # Play Podcast
        compare_titles(self, 10, [
            {'class':'', 'value':'Play'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_titles(self, 11, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Cortex'},
        ])
        compare_titles(self, 12, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Podcast','glyph':'assets/cat/Ask.svg'},
        ])
        # Sub to Podcast
        compare_titles(self, 13, [
            {'class':'', 'value':'Subscribe to'},
            {'class':'magic empty', 'value':'Podcast URL'},
        ])
        compare_titles(self, 14, [
            {'class':'', 'value':'Subscribe to'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 15, [
            {'class':'', 'value':'Subscribe to'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
            {'class':'magic', 'value':'Text','glyph':'assets/cat/Ask.svg'},
        ])
        
        
        