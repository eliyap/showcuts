## Dependency: django testss
from django.test import TestCase

## Dependency: models for testing
from ..models import Shortcut

pk='ffffffffffffffffffffffffffffffff'

class ShortcutTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Shortcut.objects.create(
            iCloud='https://www.icloud.com/shortcuts/' + pk,
            iCloudID=pk,
            download_link='https://cvws.icloud-content.com/B/AUfAj59DvD5fAY8RNlW1SM3lTout/b96b5b1801994aa08c2e8cd064b69f6e?o=AkipWEjlm_5djNcnXYYadmaf8C1QFgWPCdDpUD5LB3WTfVlkajaE_KbckKaatDx5AA&v=1&x=3&a=CAxgR8Zmn-R_qDQOkcuutplE0lViyaD9LGfMEK_xyLkEAd8SFxC_2dyP6C0Yv7a4kegtIgEAUgTlTout&e=1574142090&k=_&fl=&r=88b6ca3c-26ea-4e6e-8808-48c7646a8f19-1&ckc=com.apple.shortcuts&ckz=_defaultZone&p=33&s=kBbWxP0bSEIJgtojb3q-x1cw7lw',
            action_blocks={'blocks':[]}, 
            UUID_glyphs={},
            #TODO accept categories later
            #TODO accept tags later
            name='Test Shortcut',
            glyphID=0,
            colorID=0,
        )
    
    def test_iCloud_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('iCloud').verbose_name
        self.assertEqual(field_label, 'iCloud link')

    def test_iCloudID_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('iCloudID').verbose_name
        self.assertEqual(field_label, 'iCloud ID')
    
    def test_download_link_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('download_link').verbose_name
        self.assertEqual(field_label, 'Download Link')
    
    def test_action_blocks_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('action_blocks').verbose_name
        self.assertEqual(field_label, 'Shortcut Actions')
    
    def test_UUID_glyphs_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('UUID_glyphs').verbose_name
        self.assertEqual(field_label, 'UUID Glyphs')
    
    def test_name_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')
    
    def test_glyphID_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('glyphID').verbose_name
        self.assertEqual(field_label, 'Glyph ID')
    
    def test_colorID_label(self):
        shortcut = Shortcut.objects.get(iCloudID=pk)
        field_label = shortcut._meta.get_field('colorID').verbose_name
        self.assertEqual(field_label, 'Color ID')