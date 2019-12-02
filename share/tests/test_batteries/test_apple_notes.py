## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *


class test_apple_notes(TestCase):
    reference_image = ''
    actionID = '1c64f0b1cd3246c098c552f16b5169da'

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
        [test_correct_glyph(self, action, 'Notes.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'NOTES') for action in self.actions]


    def test_titles_correct(self):
        # Append X to Y
        compare_elements(self, 'title', 0, [
            {'class':'', 'value':'Append'},
            {'class':'magic empty', 'value':'Text'},
            {'class':'', 'value':'to'},
            {'class':'magic empty', 'value':'Note'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':'', 'value':'Append'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
            {'class':'', 'value':'to'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':'', 'value':'Append'},
            {'class':'magic', 'value':'Text','glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'to'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        # Create note with X (in Y)
        compare_elements(self, 'title', 3, [
            {'class':'', 'value':'Create note with'},
            {'class':'magic empty', 'value':'Body'},
            {'class':'', 'value':'in'},
            {'class':'magic empty', 'value':'Folder'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':'', 'value':'Create note with'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
            {'class':'', 'value':'in'},
            {'class':'magic empty', 'value':'Folder'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':'', 'value':'Create note with'},
            {'class':'magic', 'value':'Text','glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'in'},
            {'class':'magic', 'value':'Folder','glyph':'assets/cat/Ask.svg'},
        ])
        compare_elements(self, 'title', 6, [
            {'class':'', 'value':'Create note with'},
            {'class':'magic empty', 'value':'Body'},
        ])
        # Show Note
        compare_elements(self, 'title', 7, [
            {'class':'', 'value':'Show'},
            {'class':'magic empty', 'value':'Note'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':'', 'value':'Show'},
            {'class':'magic', 'value':'Clipboard','glyph':'assets/cat/Clipboard.svg'},
        ])
        