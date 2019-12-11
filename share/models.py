## Dependency: sys
from datetime import datetime

# boilerplate
from django.contrib.auth.models import User
from django.db import models

# JSONField
from django.core.serializers.json import DjangoJSONEncoder
import json

# social auth

def byt_catcher(o):
    if isinstance(o, datetime):
        return o.__str__()
    else:
        return o.decode('UTF-8')

class JSONField(models.TextField):
    def to_python(self, value):
        if value == "":
            return None
        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass
        return value

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_db_prep_save(self, value, *args, **kwargs):
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder, default=byt_catcher)
        return value

class Shortcut(models.Model):
    '''represents an iOS Siri Shortcut'''
    iCloud = models.URLField(
        'iCloud link',
        'iCloud',
        max_length=100, # should be ~65 chars
        help_text='iCloud link created by Sharing your Shortcut'
    )
    iCloudID = models.CharField(
        'iCloud ID',
        max_length = 50, # should be 32 Hexadecimal chars
        primary_key=True,
    )
    # credit: insideGUI
    # https://github.com/sharecuts/website/blob/master/Docs/Download%20shortcut%20shared%20as%20a%20link.txt
    download_link = models.URLField(
        'Download Link',
        'download_link',
        max_length=600, # ~400 chars, need to include Auth info
    )
    action_blocks = JSONField(
        'Shortcut Actions',
        'action_blocks',
        default={},
    )
    UUID_glyphs = JSONField(
        'UUID Glyphs',
        'UUID_glyphs',
        default={},
    )
    #TODO implement comments later
    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        help_text='Pick a Category to help others find your Shortcut',
    )
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        null=True,
        help_text='Tag your Shortcut to help others find it',
    )
    name = models.CharField(
        'Name',
        max_length=100,
    )
    glyphID = models.PositiveIntegerField(
        'Glyph ID',
        default=59771, # magic wand glyph
    )
    colorID = models.PositiveIntegerField(
        'Color ID',
        default=431817727, # some valid color
    )
    shortcut_types = models.CharField(
        'Shortcut Types',
        'shortcut_types',
        max_length=200,
        default='',
    )
    accepted_types = models.CharField(
        'Accepts',
        'accepted_types',
        max_length=1000, # there are a lot of possible inputs, typical length ~600char
        default='',
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
    )
    created_on = models.DateTimeField(
        'Created On',
        'created_on',
        auto_now=False,
        auto_now_add=True,
    )
    liked_by = models.ManyToManyField(
        User,
        related_name="liked",
        related_query_name="liked",
    )
    saved_by = models.ManyToManyField(
        User,
        related_name="saved",
        related_query_name="saved",
    )
    # add date submitted field
    # add number of likes field
    # add bookmarks field
    def __str__(self):
        return f'{self.name}, ID {self.iCloudID}'

    def get_absolute_url(self):
        # URL is linked to hexademical ID, nothing needed here
        pass

    class Meta:
        ordering = ['-created_on']

# I think this will help search by category?
class Category(models.Model):
    CATEGORIES = (
        '📝 Notes',
        '🌐 Web Services',
        # etc.
    ) # add these as choices later
    name = models.CharField(
        'Name',
        max_length = 50,
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # TODO: IMPLEMENT URL LOOKUP!
        pass

# I think this will help search by tag?
class Tag(models.Model):
    name = models.CharField(
        'Name',
        max_length = 50,
    )
    def __str__(self):
        return self.name

