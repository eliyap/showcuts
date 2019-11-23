## Dependency: django
from django.test import TestCase
from django.urls import reverse

## Dependency: views for testing
from ..views import submit_iCloud

## Dependency: shortcut to populate
from ..models import Shortcut

pk='ffffffffffffffffffffffffffffffff'

class submit_iCloud_Test(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_submit_locations(self):
        response = self.client.get('/share/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/share') # redirects
        self.assertTrue(response.status_code in [200, 301])
        response = self.client.get('/share/submit')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/share/view')
        self.assertEqual(response.status_code, 200)

    def test_submit_reverse(self):
        response = self.client.get(reverse('submit'))

    def test_view_locations(self):
        response = self.client.get('/share/view/'+pk)
        self.assertEqual(response.status_code, 200)

    def test_view_reverse(self):
        response = self.client.get(reverse('view',kwargs={'hxid':pk}))

    