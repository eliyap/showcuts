## Dependency: sys
from unittest import TestCase
import logging

# Dependency: battery testing
from share.tests.test_batteries.battery import *

actionID = 'faedd7efe2894db9b99425245906b894'

class test_play_music(TestCase):
    '''Tests for Play Music action.
    
    Written 20.01.11
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
                'value': 'Play',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },
        ])
        compare_elements(self, 'lines', 0, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'Off',
                    },{
                        'class':'pill-off',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'None',
                    },{
                        'class':'pill-off',
                        'value':'One',
                    },{
                        'class':'pill-off',
                        'value':'All',
                    }
                ],
            },
        ])

        compare_elements(self, 'title', 1, [
            {
                'class': ['text'], 
                'value': 'Play',
            },{
                'class': ['magic','empty'], 
                'value': 'Music',
            },
        ])
        compare_elements(self, 'lines', 1, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'Off',
                    },{
                        'class':'pill-off',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'None',
                    },{
                        'class':'pill-off',
                        'value':'One',
                    },{
                        'class':'pill-off',
                        'value':'All',
                    }
                ],
            },
        ])
       
        compare_elements(self, 'title', 2, [
            {
                'class': ['text'], 
                'value': 'Play',
            },{
                'class': ['magic'], 
                'value': 'Music',
            },
        ])
        compare_elements(self, 'lines', 2, [
            {
                'label':'Shuffle',
                'class': ['magic'], 
                'value': 'Ask Each Time',
            },{
                'label':'Repeat',
                'class': ['magic'], 
                'value': 'Ask Each Time',
            },
        ])

        compare_elements(self, 'title', 3, [
            {
                'class': ['text'], 
                'value': 'Play',
            },{
                'class': ['magic'], 
                'value': 'Beats 1',
            },
        ])

        compare_elements(self, 'title', 4, [
            {
                'class': ['text'], 
                'value': 'Play',
            },{
                'class': ['magic'], 
                'value': 'Kitty',
            },
        ])

        compare_elements(self, 'lines', 5, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-on',
                        'value':'Off',
                    },{
                        'class':'pill-off',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'None',
                    },{
                        'class':'pill-off',
                        'value':'One',
                    },{
                        'class':'pill-off',
                        'value':'All',
                    }
                ],
            },
        ])

        compare_elements(self, 'lines', 6, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'Off',
                    },{
                        'class':'pill-on',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'None',
                    },{
                        'class':'pill-off',
                        'value':'One',
                    },{
                        'class':'pill-off',
                        'value':'All',
                    }
                ],
            },
        ])
        
        compare_elements(self, 'lines', 7, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'Off',
                    },{
                        'class':'pill-off',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-on',
                        'value':'None',
                    },{
                        'class':'pill-off',
                        'value':'One',
                    },{
                        'class':'pill-off',
                        'value':'All',
                    }
                ],
            },
        ])
        
        compare_elements(self, 'lines', 8, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'Off',
                    },{
                        'class':'pill-off',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'None',
                    },{
                        'class':'pill-on',
                        'value':'One',
                    },{
                        'class':'pill-off',
                        'value':'All',
                    }
                ],
            },
        ])
        
        compare_elements(self, 'lines', 9, [
            {
                'label':'Shuffle',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'Off',
                    },{
                        'class':'pill-off',
                        'value':'Songs',
                    }
                ],
            },{
                'label':'Repeat',
                'class': ['pill'], 
                'value': [
                    {
                        'class':'pill-off',
                        'value':'None',
                    },{
                        'class':'pill-off',
                        'value':'One',
                    },{
                        'class':'pill-on',
                        'value':'All',
                    }
                ],
            },
        ])