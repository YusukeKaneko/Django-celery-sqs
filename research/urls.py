from django.urls import path

from . import views


urlpatterns = [
    path('translate/', views.TranslateAPIView.as_view(), name='translations_translate'),
    path('translate/<uuid:id>/',  views.TranslatedAPIView.as_view(), name='translations_translated'),
]
