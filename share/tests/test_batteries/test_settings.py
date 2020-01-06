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
        compare_elements(self, 'title', 0, [
            {'class':['text'], 'value':'Open Magnifier'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':['text'], 'value':'Start Guided Access'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':['text'], 'value':'Start Speak Screen'},
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
        compare_elements(self, 'title', 0, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'extra small'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'small'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'medium'},
        ])
        compare_elements(self, 'title', 3, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'default'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'extra large'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'extra extra large'},
        ])
        compare_elements(self, 'title', 6, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'extra extra extra large'},
        ])
        compare_elements(self, 'title', 7, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'accessibility medium'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'accessibility large'},
        ])
        compare_elements(self, 'title', 9, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'accessibility extra large'},
        ])
        compare_elements(self, 'title', 10, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'accessibility extra extra large'},
        ])
        compare_elements(self, 'title', 11, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'accessibility extra extra extra large'},
        ])
        compare_elements(self, 'title', 12, [
            {'class':['text'], 'value':'Set text size to'},
            {'class':['magic'], 'value':'Text Size'},
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
        compare_elements(self, 'title', 0, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'AssistiveTouch'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Audio Descriptions'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Classic Invert'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 3, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Closed Captions+SDH'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Increase Contrast'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'LED Flash'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 6, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Mono Audio'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 7, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Reduce Motion'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Reduce Transparency'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 9, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Smart Invert'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 10, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Switch Control'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 11, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Voice Control'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 12, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'VoiceOver'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 13, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'White Point'},
            {'class':['magic'], 'value':'State'},
        ])
        compare_elements(self, 'title', 14, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Zoom'},
            {'class':['magic'], 'value':'State'},
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
        compare_elements(self, 'title', 0, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'AssistiveTouch'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Audio Descriptions'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Classic Invert'},
            {'class':['magic'], 'value':'off'},
        ])
        compare_elements(self, 'title', 3, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Closed Captions+SDH'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Increase Contrast'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'LED Flash'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 6, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Mono Audio'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 7, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Reduce Motion'},
            {'class':['magic'], 'value':'off'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Reduce Transparency'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 9, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Smart Invert'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 10, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Switch Control'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 11, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Voice Control'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 12, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'VoiceOver'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 13, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'White Point'},
            {'class':['magic'], 'value':'on'},
        ])
        compare_elements(self, 'title', 14, [
            {'class':['magic'], 'value':'Turn'},
            {'class':['text'], 'value':'Zoom'},
            {'class':['magic'], 'value':'on'},
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
        compare_elements(self, 'title', 0, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'AssistiveTouch'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 1, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Audio Descriptions'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 2, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Classic Invert'},
            {'class':['magic','hidden'], 'value':'off'},
        ])
        compare_elements(self, 'title', 3, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Closed Captions+SDH'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 4, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Increase Contrast'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 5, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'LED Flash'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 6, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Mono Audio'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 7, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Reduce Motion'},
            {'class':['magic','hidden'], 'value':'off'},
        ])
        compare_elements(self, 'title', 8, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Reduce Transparency'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 9, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Smart Invert'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 10, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Switch Control'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 11, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Voice Control'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 12, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'VoiceOver'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 13, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'White Point'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        compare_elements(self, 'title', 14, [
            {'class':['magic'], 'value':'Operation'},
            {'class':['text'], 'value':'Zoom'},
            {'class':['magic','hidden'], 'value':'on'},
        ])
        