## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *


class test_simple_settings(TestCase):
    reference_image = 'https://i.imgur.com/eJTtRgZ.jpg'
    actionID = '3bc77e514fb241939e0111349aa3718a'

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
        [test_correct_glyph(self, action, 'Settings.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'SETTINGS') for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'', 'value':'Open Magnifier'},
        ])
        compare_titles(self, 1, [
            {'class':'', 'value':'Start Guided Access'},
        ])
        compare_titles(self, 2, [
            {'class':'', 'value':'Start Speak Screen'},
        ])
        
class test_text_size(TestCase):
    reference_image = '' # stitching failed
    actionID = '1d3f4f25d7a8451c8a453a9b66fc85e4'

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
        [test_correct_glyph(self, action, 'Settings.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'SETTINGS') for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'extra small'},
        ])
        compare_titles(self, 1, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'small'},
        ])
        compare_titles(self, 2, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'medium'},
        ])
        compare_titles(self, 3, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'default'},
        ])
        compare_titles(self, 4, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'extra large'},
        ])
        compare_titles(self, 5, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'extra extra large'},
        ])
        compare_titles(self, 6, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'extra extra extra large'},
        ])
        compare_titles(self, 7, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'accessibility medium'},
        ])
        compare_titles(self, 8, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'accessibility large'},
        ])
        compare_titles(self, 9, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'accessibility extra large'},
        ])
        compare_titles(self, 10, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'accessibility extra extra large'},
        ])
        compare_titles(self, 11, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'accessibility extra extra extra large'},
        ])
        compare_titles(self, 12, [
            {'class':'', 'value':'Set text size to'},
            {'class':'magic', 'value':'Text Size'},
        ])
        
class test_settings_state(TestCase):
    reference_image = 'https://i.imgur.com/xLv8ICS.png'
    actionID = 'f3970902f90f48ba991fb4e76743920e'

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
        [test_correct_glyph(self, action, 'Settings.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'SETTINGS') for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'AssistiveTouch'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 1, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Audio Descriptions'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 2, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Classic Invert'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 3, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Closed Captions+SDH'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 4, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Increase Contrast'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 5, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'LED Flash'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 6, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Mono Audio'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 7, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Reduce Motion'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 8, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Reduce Transparency'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 9, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Smart Invert'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 10, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Switch Control'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 11, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Voice Control'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 12, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'VoiceOver'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 13, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'White Point'},
            {'class':'magic', 'value':'State'},
        ])
        compare_titles(self, 14, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Zoom'},
            {'class':'magic', 'value':'State'},
        ])
        
class test_settings_default(TestCase):
    reference_image = 'https://i.imgur.com/yZhKm0N.png'
    actionID = '458086c486fd485cbf1917a06e2c09cd'

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
        [test_correct_glyph(self, action, 'Settings.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'SETTINGS') for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'AssistiveTouch'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 1, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Audio Descriptions'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 2, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Classic Invert'},
            {'class':'magic', 'value':'off'},
        ])
        compare_titles(self, 3, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Closed Captions+SDH'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 4, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Increase Contrast'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 5, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'LED Flash'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 6, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Mono Audio'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 7, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Reduce Motion'},
            {'class':'magic', 'value':'off'},
        ])
        compare_titles(self, 8, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Reduce Transparency'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 9, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Smart Invert'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 10, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Switch Control'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 11, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Voice Control'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 12, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'VoiceOver'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 13, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'White Point'},
            {'class':'magic', 'value':'on'},
        ])
        compare_titles(self, 14, [
            {'class':'magic', 'value':'Turn'},
            {'class':'', 'value':'Zoom'},
            {'class':'magic', 'value':'on'},
        ])
        
class test_settings_operation(TestCase):
    reference_image = 'https://i.imgur.com/FeOavuK.png'
    actionID = 'd50d574d94c74434ac8307dffdfbcfe1'

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
        [test_correct_glyph(self, action, 'Settings.png') for action in self.actions]

    def test_categoryies_correct(self):
        [self.assertEqual(action['category'], 'SETTINGS') for action in self.actions]

    def test_titles_correct(self):
        compare_titles(self, 0, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'AssistiveTouch'},
        ])
        compare_titles(self, 1, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Audio Descriptions'},
        ])
        compare_titles(self, 2, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Classic Invert'},
        ])
        compare_titles(self, 3, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Closed Captions+SDH'},
        ])
        compare_titles(self, 4, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Increase Contrast'},
        ])
        compare_titles(self, 5, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'LED Flash'},
        ])
        compare_titles(self, 6, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Mono Audio'},
        ])
        compare_titles(self, 7, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Reduce Motion'},
        ])
        compare_titles(self, 8, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Reduce Transparency'},
        ])
        compare_titles(self, 9, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Smart Invert'},
        ])
        compare_titles(self, 10, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Switch Control'},
        ])
        compare_titles(self, 11, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Voice Control'},
        ])
        compare_titles(self, 12, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'VoiceOver'},
        ])
        compare_titles(self, 13, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'White Point'},
        ])
        compare_titles(self, 14, [
            {'class':'magic', 'value':'Operation'},
            {'class':'', 'value':'Zoom'},
        ])
        