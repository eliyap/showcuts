from rest_framework import serializers
from .models import Shortcut

class ActionField(serializers.Field):
    def to_native(self,obj): # TODO: add proper to_native
        return ""
    def to_representation(self,obj):
        return obj

class IconField(serializers.Field):
    def to_representation(self,obj):
        return obj

class ShortcutSerializer(serializers.HyperlinkedModelSerializer):
    actions = ActionField(source='get_actions')
    icon = IconField(source='get_icon')
    class Meta:
        model = Shortcut
        fields = ('iCloudID', 'actions','name','icon')

