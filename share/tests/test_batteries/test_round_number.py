## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = '30ccbbbf3dfa4fd28281a60260f52a37'

class test_round_number(TestCase):
    '''Tests for Round Number action.
    
    Written 20.01.06
    '''
    # boilerplate

    def setUp(self):
        self.actions = actions_from_ID(actionID)
        # remove comment actions
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
        [test_correct_glyph(self, action, 'Math.svg')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'MATHS')
         for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Ones Place',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 0, [
            {
                'label':'Mode',
                'class': ['choose'], 
                'value': 'Normal',
            },
        ])
        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Ones Place',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 1, [
            {
                'label':'Mode',
                'class': ['choose'], 
                'value': 'Normal',
            },
        ])
        
        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic'], 
                'glyph': 'assets/cat/Ask.svg', 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'glyph': 'assets/cat/Ask.svg', 
                'value': 'Value',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 2, [
            {
                'label':'Mode',
                'class': ['magic','choose',], 
                'glyph': 'assets/cat/Ask.svg', 
                'value': 'Ask Each Time',
            },
        ])
        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Millions',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 3, [
            {
                'label':'Mode',
                'class': ['choose',], 
                'value': 'Normal',
            },
        ])
        compare_elements(self, 'title', 4, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Hundred Thousands',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 4, [
            {
                'label':'Mode',
                'class': ['choose',], 
                'value': 'Always Round Up',
            },
        ])
        
        compare_elements(self, 'title', 5, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Ten Thousands',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 5, [
            {
                'label':'Mode',
                'class': ['choose',], 
                'value': 'Always Round Down',
            },
        ])
        
        compare_elements(self, 'title', 6, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Thousands',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        compare_elements(self, 'lines', 6, [
            {
                'label':'Mode',
                'class': ['magic','choose',], 
                'glyph': 'assets/cat/Math.svg', 
                'value': 'Rounded Number',
            },
        ])
        
        compare_elements(self, 'title', 7, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Hundreds Place',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 8, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Tens Place',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 9, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Ones Place',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 10, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Tenths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 11, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Hundredths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 12, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Thousandths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 13, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Ten Thousandths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 14, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Hundred Thousandths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 15, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Millionths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 16, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Ten Millionths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 17, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Hundred Millionths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 18, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': 'Billionths',
                'field':'choose',
            },
            {
                'class': ['magic', 'hidden'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 19, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': '10 ^',
                'field':'choose',
            },
            {
                'class': ['magic','empty'], 
                'value': '',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 20, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': '10 ^',
                'field':'choose',
            },
            {
                'class': ['magic'], 
                'value': '0',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 21, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': '10 ^',
                'field':'choose',
            },
            {
                'class': ['magic'], 
                'value': '-10',
                'field':'wholenumber',
            },
        ])
        
        compare_elements(self, 'title', 22, [
            {
                'class': ['text'], 
                'value': 'Round',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Number',
                'field':'number',
            },
            {
                'class': ['text'], 
                'value': 'to',
            },
            {
                'class': ['magic'], 
                'value': '10 ^',
                'field':'choose',
            },
            {
                'class': ['magic'], 
                'value': 'Ask Each Time',
                'field':'wholenumber',
            },
        ])
        