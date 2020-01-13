## Dependency: sys
from unittest import TestCase
import logging


## Dependency: battery testing
from share.tests.test_batteries.battery import *
'''Load actions which are only tested visually.
Some actions are so simple that I only perform a visual check to see that they're
all right.

This suite simply loads all those actions to see if they run throw errors.

'''

class test_load(TestCase):
    actionIDs = [
        '1c64f0b1cd3246c098c552f16b5169da', # Trim Media
        '6f12d879df9b4784be1d1f71d35e24bc', # Clear Up Next
        '06bc19b5a33d40d983f16939ccf9cf4d', # Get Current Song
    ]

    # boilerplate

    def setUp(self):
        [actions_from_ID(actionID) for actionID in __class__.actionIDs]
