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
        compare_elements(self, 'title', 0, [
            {'class':'', 'value':'Play'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Cortex'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Podcast','glyph':'assets/cat/Ask.svg'},
        ])
        # Get Detail from Podcast
        compare_elements(self, 'title', 3, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Podcast episode'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Name'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        # Get episodes of Podcast
        compare_elements(self, 'title', 6, [
            {'class':'', 'value':'Get episodes of'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_elements(self, 'title', 7, [
            {'class':'', 'value':'Get episodes of'},
            {'class':'magic', 'value':'Cortex'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':'', 'value':'Get episodes of'},
            {'class':'magic', 'value':'Podcast','glyph':'assets/cat/Ask.svg'},
        ])
        # mono
        compare_elements(self, 'title', 9, [
            {'class':'', 'value':'Get Podcasts from Library'},
        ])
        # Play Podcast
        compare_elements(self, 'title', 10, [
            {'class':'', 'value':'Play'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_elements(self, 'title', 11, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Cortex'},
        ])
        compare_elements(self, 'title', 12, [
            {'class':'', 'value':'Play'},
            {'class':'magic', 'value':'Podcast','glyph':'assets/cat/Ask.svg'},
        ])
        # Sub to Podcast
        compare_elements(self, 'title', 13, [
            {'class':'', 'value':'Subscribe to'},
            {'class':'magic empty', 'value':'Podcast URL'},
        ])
        compare_elements(self, 'title', 14, [
            {'class':'', 'value':'Subscribe to'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_elements(self, 'title', 15, [
            {'class':'', 'value':'Subscribe to'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
            {'class':'magic', 'value':'Text','glyph':'assets/cat/Ask.svg'},
        ])
        
        
        