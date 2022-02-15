from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Translations


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 


class TranslationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translations
        fields = '__all__' 
        read_only_fields = ('created_at', 'updated_at', 'translated_text', 'finished_at', 'is_finished')
