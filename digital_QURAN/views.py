# -*- coding: UTF-8 -*-
from responses import *
from django.shortcuts import HttpResponse
from models import *
import json
from common.utils import to_epoch
from datetime import datetime
import traceback


def get_meta_data_quran_api(request):
    resp = OK()
    resp['Juz'] = [object.to_dict_api() for object in Juz.objects.all()]
    resp['Sura'] = [object.to_dict_api() for object in Sura.objects.all()]
    resp['Hizb'] = [object.to_dict_api() for object in Hizb.objects.all()]
    resp['Manzil'] = [object.to_dict_api() for object in Manzil.objects.all()]
    resp['Ruku'] = [object.to_dict_api() for object in Ruku.objects.all()]
    resp['Page'] = [object.to_dict_api() for object in Page.objects.all()]
    resp['Sajda'] = [object.to_dict_api() for object in Sajda.objects.all()]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_quran_text_quran_api_1(request, sura_number):
    resp = OK()
    resp['text'] = [obj.to_dict_api() for obj in QuranText.objects.filter(sura=int(sura_number))]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_quran_text_quran_api_2(request, sura_number, aya_number):
    resp = OK()
    resp['text'] = [obj.to_dict_api() for obj in QuranText.objects.filter(sura=int(sura_number)).filter(aya=int(aya_number))]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_translations_quran_api(request):
    resp = OK()
    resp['translations'] = [obj.to_dict_api() for obj in QuranTranslation.objects.all()]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_translation_text_quran_api_1(request, translator, sura_number):
    resp = OK()
    resp['text'] = [obj.to_dict_api() for obj in QuranTranslationText.objects.filter(tranlation__id=int(translator)).filter(sura=int(sura_number))]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_translation_text_quran_api_2(request, translator, sura_number, aya_number):
    resp = OK()
    resp['text'] = [obj.to_dict_api() for obj in QuranTranslationText.objects.filter(tranlation__id=int(translator)).filter(sura=int(sura_number)).filter(aya=int(aya_number))]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_recitations_verse_quran_api(request):
    resp = OK()
    resp['recitations_verse'] = [obj.to_dict_api() for obj in RecitationVerseByVerse.objects.all()]
    return HttpResponse(json.dumps(resp), content_type='application/json')

def get_recitations_page_quran_api(request):
    resp = OK()
    resp['recitations_page'] = [obj.to_dict_api() for obj in RecitationPageByPage.objects.all()]
    return HttpResponse(json.dumps(resp), content_type='application/json')




