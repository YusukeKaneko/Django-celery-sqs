from config.tasks import translate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response

from .models import Translations
from .serializers import TranslationsSerializer, UsersSerializer


class TranslateAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        user_data = get_object_or_404(User, username=self.request.user.username)
        serializer = UsersSerializer(user_data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TranslationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        translate.delay(serializer.data['id'])
        return Response({"id":serializer.data['id']}, status=status.HTTP_202_ACCEPTED)


class TranslatedAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        translation_data = Translations.objects.get(id=self.kwargs['id'])
        serializer = TranslationsSerializer(translation_data)
        return Response(serializer.data)
