## Dependency: sys
import html, re

## Dependency: tests
from django.test import TestCase
import logging

## Dependency: forms for testing
from ..forms import iCloudForm

def check_iCloud_error_message(self, data:dict, expected_error:str):
    form = iCloudForm(data=data)
    try:
        self.assertTrue(expected_error in html.unescape(str(form.errors)))
    except AssertionError:
        logging.error(html.unescape(str(form.errors)))
        logging.error(data, expected_error)
        raise AssertionError
    #self.assertTrue(form.has_error('iCloudLink',code=expected_error))

class iCloudFormTest(TestCase):
    def test_iCloud_link_help_text(self):
        form = iCloudForm()
        self.assertEqual(form.fields['iCloudLink'].help_text, 'Enter an Shortcut iCloud link')
        
    def test_rejects_non_iCloud_link(self):
        check_iCloud_error_message(self, 
            {'iCloudLink':'https://goose.game/'}, 
            'Please enter an iCloud link'
        )

    def test_accepts_no_https_no_www(self):
        form = iCloudForm(data={'iCloudLink':'icloud.com/shortcuts/893ec0790cc14cc1a497720c29d48775'})
        self.assertTrue(form.is_valid())

    def test_rejects_short_link(self):
        check_iCloud_error_message(self, 
            {'iCloudLink':'https://www.icloud.com/shortcuts/cba1b71ad1174897ad528bfbbd027212'[:-1]}, 
            'Link doesn\'t contain a valid Shortcut ID'
        )
    
    def test_rejects_long_link(self):
        check_iCloud_error_message(self, 
            {'iCloudLink':'https://www.icloud.com/shortcuts/cba1b71ad1174897ad528bfbbd027212'+'0'}, 
            'Link doesn\'t contain a valid Shortcut ID'
        )

    def test_rejects_non_hexadecimal(self):
        link = re.sub(
            '1','g',
            'https://www.icloud.com/shortcuts/cba1b71ad1174897ad528bfbbd027212'
        )
        check_iCloud_error_message(self, 
            {'iCloudLink':link}, 
            'Link doesn\'t contain a valid Shortcut ID'
        )

    def test_accepts_trailing_spaces(self):
        link = 'https://www.icloud.com/shortcuts/cba1b71ad1174897ad528bfbbd027212'
        form = iCloudForm(data={'iCloudLink':link + ' '})
        self.assertTrue(form.is_valid())

        form = iCloudForm(data={'iCloudLink':link + '  '})
        self.assertTrue(form.is_valid())

    def test_rejects_non_links(self):
        check_iCloud_error_message(self, 
            {'iCloudLink':'this is not a URL'}, 
            'Please enter an iCloud link'
        )