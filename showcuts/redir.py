from django.urls import reverse
from django.views.generic import RedirectView
from django.http import QueryDict

class front_with_query(RedirectView):

    def get_redirect_url(self):
        q = self.request.GET
        if not q: return (reverse('submit'))
        hxid = q['state'].split('_')[0]
        return reverse('reddit', kwargs={'hxid':hxid}) + '?' + q.urlencode()
