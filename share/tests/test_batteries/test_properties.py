## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *


class test_properties_blank(TestCase):
    reference_image = ''
    actionID = '0d0efe1b145c42d79ed57b56fd544194'

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
        test_correct_glyph(self, self.actions[0], 'Trello.png')
        test_correct_glyph(self, self.actions[1], 'File.svg')
        test_correct_glyph(self, self.actions[2], 'iTunes.svg')
        test_correct_glyph(self, self.actions[3], 'iTunes.svg')
        test_correct_glyph(self, self.actions[4], 'Podcasts.png')
        test_correct_glyph(self, self.actions[5], 'AppStore.jpg')
        test_correct_glyph(self, self.actions[6], 'Image.svg')
        test_correct_glyph(self, self.actions[7], 'Ulysses.png')
        test_correct_glyph(self, self.actions[8], 'Music.png')
        test_correct_glyph(self, self.actions[9], 'Podcasts.png')
        test_correct_glyph(self, self.actions[10], 'Weather.png')
        test_correct_glyph(self, self.actions[11], 'Location.svg')
        test_correct_glyph(self, self.actions[12], 'Calendar.jpg')
        test_correct_glyph(self, self.actions[13], 'Calendar.jpg')
        test_correct_glyph(self, self.actions[14], 'Reminders.png')
        test_correct_glyph(self, self.actions[15], 'Health.jpg')
        test_correct_glyph(self, self.actions[16], 'Contacts.png')
        test_correct_glyph(self, self.actions[17], 'Safari.jpg')
        test_correct_glyph(self, self.actions[18], 'Safari.jpg')

    def test_categoryies_correct(self):
        self.assertEqual(self.actions[0]['category'], 'TRELLO')
        self.assertEqual(self.actions[1]['category'], 'DOCUMENTS')
        self.assertEqual(self.actions[2]['category'], 'ITUNES STORE')
        self.assertEqual(self.actions[3]['category'], 'ITUNES STORE')
        self.assertEqual(self.actions[4]['category'], 'PODCASTS')
        self.assertEqual(self.actions[5]['category'], 'APP STORE')
        self.assertEqual(self.actions[6]['category'], 'MEDIA')
        self.assertEqual(self.actions[7]['category'], 'ULYSSES')
        self.assertEqual(self.actions[8]['category'], 'MUSIC')
        self.assertEqual(self.actions[9]['category'], 'PODCASTS')
        self.assertEqual(self.actions[10]['category'], 'LOCATION')
        self.assertEqual(self.actions[11]['category'], 'LOCATION')
        self.assertEqual(self.actions[12]['category'], 'CALENDAR')
        self.assertEqual(self.actions[13]['category'], 'CALENDAR')
        self.assertEqual(self.actions[14]['category'], 'REMINDERS')
        self.assertEqual(self.actions[15]['category'], 'HEALTH')
        self.assertEqual(self.actions[16]['category'], 'CONTACTS')
        self.assertEqual(self.actions[17]['category'], 'SAFARI')
        self.assertEqual(self.actions[18]['category'], 'SAFARI')

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Trello item'},
        ])
        compare_titles(self, 1, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'File'},
        ])
        compare_titles(self, 2, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'iTunes product'},
        ])
        compare_titles(self, 3, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'iTunes artist'},
        ])
        compare_titles(self, 4, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Podcast episode'},
        ])
        compare_titles(self, 5, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'App Store app'},
        ])
        compare_titles(self, 6, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Image'},
        ])
        compare_titles(self, 7, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Ulysses sheet'},
        ])
        compare_titles(self, 8, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Artist'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Music'},
        ])
        compare_titles(self, 9, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Podcast'},
        ])
        compare_titles(self, 10, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Weather Conditions'},
        ])
        compare_titles(self, 11, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Location'},
        ])
        compare_titles(self, 12, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Event Attendee'},
        ])
        compare_titles(self, 13, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Calendar Event'},
        ])
        compare_titles(self, 14, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'List'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Reminder'},
        ])
        compare_titles(self, 15, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Health Sample'},
        ])
        compare_titles(self, 16, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Contact'},
        ])
        compare_titles(self, 17, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Article'},
        ])
        compare_titles(self, 18, [
            {'class':'', 'value':'Get'},
            {'class':'magic empty', 'value':'Detail'},
            {'class':'', 'value':'from'},
            {'class':'magic empty', 'value':'Safari web page'},
        ])

class test_properties_magic(TestCase):
    reference_image = ''
    actionID = '3b24ad8f20cc45288b9333aec113fed4'

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
        test_correct_glyph(self, self.actions[0], 'Trello.png')
        test_correct_glyph(self, self.actions[1], 'File.svg')
        test_correct_glyph(self, self.actions[2], 'iTunes.svg')
        test_correct_glyph(self, self.actions[3], 'iTunes.svg')
        test_correct_glyph(self, self.actions[4], 'Podcasts.png')
        test_correct_glyph(self, self.actions[5], 'AppStore.jpg')
        test_correct_glyph(self, self.actions[6], 'Image.svg')
        test_correct_glyph(self, self.actions[7], 'Ulysses.png')
        test_correct_glyph(self, self.actions[8], 'Music.png')
        test_correct_glyph(self, self.actions[9], 'Podcasts.png')
        test_correct_glyph(self, self.actions[10], 'Weather.png')
        test_correct_glyph(self, self.actions[11], 'Location.svg')
        test_correct_glyph(self, self.actions[12], 'Calendar.jpg')
        test_correct_glyph(self, self.actions[13], 'Calendar.jpg')
        test_correct_glyph(self, self.actions[14], 'Reminders.png')
        test_correct_glyph(self, self.actions[15], 'Health.jpg')
        test_correct_glyph(self, self.actions[16], 'Contacts.png')
        test_correct_glyph(self, self.actions[17], 'Safari.jpg')
        test_correct_glyph(self, self.actions[18], 'Safari.jpg')

    def test_categoryies_correct(self):
        self.assertEqual(self.actions[0]['category'], 'TRELLO')
        self.assertEqual(self.actions[1]['category'], 'DOCUMENTS')
        self.assertEqual(self.actions[2]['category'], 'ITUNES STORE')
        self.assertEqual(self.actions[3]['category'], 'ITUNES STORE')
        self.assertEqual(self.actions[4]['category'], 'PODCASTS')
        self.assertEqual(self.actions[5]['category'], 'APP STORE')
        self.assertEqual(self.actions[6]['category'], 'MEDIA')
        self.assertEqual(self.actions[7]['category'], 'ULYSSES')
        self.assertEqual(self.actions[8]['category'], 'MUSIC')
        self.assertEqual(self.actions[9]['category'], 'PODCASTS')
        self.assertEqual(self.actions[10]['category'], 'LOCATION')
        self.assertEqual(self.actions[11]['category'], 'LOCATION')
        self.assertEqual(self.actions[12]['category'], 'CALENDAR')
        self.assertEqual(self.actions[13]['category'], 'CALENDAR')
        self.assertEqual(self.actions[14]['category'], 'REMINDERS')
        self.assertEqual(self.actions[15]['category'], 'HEALTH')
        self.assertEqual(self.actions[16]['category'], 'CONTACTS')
        self.assertEqual(self.actions[17]['category'], 'SAFARI')
        self.assertEqual(self.actions[18]['category'], 'SAFARI')

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 1, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 2, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 3, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 4, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 5, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 6, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 7, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 8, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 9, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 10, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 11, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 12, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 13, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 14, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 15, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 16, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 17, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])
        compare_titles(self, 18, [
            {'class':'', 'value':'Get'},
            {'class':'magic', 'value':'Detail', 'glyph':'assets/cat/Ask.svg'},
            {'class':'', 'value':'from'},
            {'class':'magic', 'value':'Clipboard', 'glyph':'assets/cat/Clipboard.svg'},
        ])