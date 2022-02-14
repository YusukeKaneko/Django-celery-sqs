from __future__ import absolute_import, unicode_literals

import time

from django.shortcuts import get_object_or_404
from django.utils import timezone
from research.models import Translations

from celery import shared_task


@shared_task
def translate(id):
    time.sleep(10)
    translation_data = get_object_or_404(Translations, id=id)
    translated_text = translation_data.input_text + ' by me'
    translation_data.translated_text = translated_text
    translation_data.finished_at = timezone.now()
    translation_data.is_finished = True
    translation_data.save()
