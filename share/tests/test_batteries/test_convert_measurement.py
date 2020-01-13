## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = 'c27de7c1d81444069f6c6b67459ff661'

class test_convert_measurement(TestCase):
    '''Tests for Convert Measurement action.
    
    Written 20.01.07
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
        [test_correct_glyph(self, action, 'Math.svg')
         for action in self.actions]

    def test_categories_correct(self):
        [self.assertEqual(action['category'], 'MEASUREMENT')
         for action in self.actions]

    def test_titles_correct(self):
        compare_elements(self, 'title', 0, [
            {
                'class': ['text'], 
                'value': 'Convert',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Measurement',
                'field':'magic',
            },
            {
                'class': ['text'], 
                'value': 'into',
            },
            {
                'class': ['magic'], 
                'value': 'Length',
                'field':'choose',
            },
            {
                'class': ['text'], 
                'value': 'in',
            },
            {
                'class': ['magic'], 
                'value': 'metres',
                'field':'unit',
            },
        ])
        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Convert',
            },
            {
                'class': ['magic', 'empty'], 
                'value': 'Measurement',
                'field':'magic',
            },
            {
                'class': ['text'], 
                'value': 'into',
            },
            {
                'class': ['magic'], 
                'value': 'Length',
                'field':'choose',
            },
            {
                'class': ['text'], 
                'value': 'in',
            },
            {
                'class': ['magic'], 
                'value': 'metres',
                'field':'unit',
            },
        ])
        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Convert',
            },{
                'class': ['magic', 'empty'], 
                'value': 'Measurement',
                'field':'magic',
            },{
                'class': ['text'], 
                'value': 'into',
            },{
                'class': ['magic'], 
                'value': 'Type',
                'field':'choose',
                'glyph':'assets/cat/Ask.svg',
            },{
                'class': ['text','hidden'], 
                'value': 'in',
            },{
                'class': ['magic','hidden'], 
                'value': 'Unit', # PLACEHOLDER VALUE
                'field':'unit',
            },
        ])
        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Convert',
            },
            {
                'class': ['magic'], 
                'value': 'Clipboard',
                'field':'magic',
            },
            {
                'class': ['text'], 
                'value': 'into',
            },
            {
                'class': ['magic'], 
                'value': 'Length',
                'field':'choose',
            },
            {
                'class': ['text'], 
                'value': 'in',
            },
            {
                'class': ['magic'], 
                'value': 'metres',
                'field':'unit',
            },
        ])
        compare_elements(self, 'title', 4, [
            {
                'class': ['text'], 
                'value': 'Convert',
            },
            {
                'class': ['magic','empty'], 
                'value': 'Measurement',
                'field':'magic',
            },
            {
                'class': ['text'], 
                'value': 'into',
            },
            {
                'class': ['magic'], 
                'value': 'Length',
                'field':'choose',
            },
            {
                'class': ['text'], 
                'value': 'in',
            },
            {
                'class': ['magic'], 
                'value': 'Converted Measurement',
                'field':'unit',
            },
        ])
        compare_elements(self, 'title', 5, [
            {
                'class': ['text'], 
                'value': 'Convert',
            },
            {
                'class': ['magic'], 
                'value': 'Converted Measurement',
                'field':'magic',
            },
            {
                'class': ['text'], 
                'value': 'into',
            },
            {
                'class': ['magic'], 
                'value': 'Length',
                'field':'choose',
            },
            {
                'class': ['text'], 
                'value': 'in',
            },
            {
                'class': ['magic'], 
                'value': 'Unit',
                'field':'unit',
            },
        ])